from confluent_kafka import Consumer, KafkaError, Producer
import json
from datetime import datetime, timedelta

def create_consumer(bootstrap_servers, group_id, auto_offset_reset='earliest'):
    """Create a Kafka consumer instance."""
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'group.id': group_id,
        'auto.offset.reset': auto_offset_reset
    }
    return Consumer(conf)

def create_producer(bootstrap_servers):
    """Create a Kafka producer instance."""
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'client.id': 'python_producer'
    }
    return Producer(conf)

def process_checkpoint(message, last_checkpoints):
    """Process a checkpoint message and calculate segment pace."""
    try:
        checkpoint_data = json.loads(message.value())
        runner_id = checkpoint_data.get('runner_id')

        # Extract the last checkpoint for the runner_id
        previous_checkpoint = last_checkpoints.get(runner_id, '00:00:00')

        # Convert time strings to timedelta objects
        current_checkpoint = datetime.strptime(checkpoint_data['current_checkpoint'], "%H:%M:%S")
        previous_checkpoint_time = datetime.strptime(previous_checkpoint, "%H:%M:%S")

        # Calculate time difference in minutes
        time_difference = (current_checkpoint - previous_checkpoint_time).total_seconds() / 60

        # Convert elap_distance to float
        elap_distance = float(checkpoint_data.get('elap_distance', 0.0))

        # Calculate segment pace in minutes per kilometer
        segment_pace = time_difference / elap_distance if elap_distance != 0 else 0.0

        # Update the payload with previous_checkpoint and segment_pace
        checkpoint_data['previous_checkpoint'] = previous_checkpoint
        checkpoint_data['segment_pace'] = segment_pace

        return checkpoint_data

    except Exception as e:
        print(f"Error processing checkpoint: {e}")
        return None

def consume_messages(consumer, producer, input_topic, output_topic):
    """Consume messages from the input topic, process, and produce to the output topic."""
    last_checkpoints = {}

    consumer.subscribe([input_topic])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        checkpoint_data = process_checkpoint(msg, last_checkpoints)

        if checkpoint_data:
            # Produce the processed message to the output topic
            producer.produce(output_topic, key=checkpoint_data['runner_id'], value=json.dumps(checkpoint_data))

            # Update the last checkpoint for the specific runner_id
            last_checkpoints[checkpoint_data['runner_id']] = checkpoint_data['current_checkpoint']

            print(f"Processed message: {checkpoint_data}")

        producer.flush()

if __name__ == "__main__":
    bootstrap_servers = 'localhost:9092'
    group_id = 'checkpoints_consumer_group'
    input_topic = 'checkpoints_log'
    output_topic = 'processed_checkpoints'

    consumer = create_consumer(bootstrap_servers, group_id)
    producer = create_producer(bootstrap_servers)

    try:
        consume_messages(consumer, producer, input_topic, output_topic)

    except KeyboardInterrupt:
        pass

    finally:
        consumer.close()
        producer.flush()
