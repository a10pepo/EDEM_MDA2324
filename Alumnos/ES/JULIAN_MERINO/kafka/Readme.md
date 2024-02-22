### KAFKA POSTWORK DELIVERABLE - JULIÁN MERINO PÉREZ###

Following the trail-running topic used in Spark work, this exercise replicates the data sent from the bib checkpoints in Ultra-Trail du Mont Blanc (UTMB) 100-miles race.
A docker-compose yaml file is recycled to set-up kafka, kafka-ui, ksql-server, ksql-cli
   
    Producer:   To simulate the runners passing through the checkpoints, a CSV file contains the elapsed distance (elap_distance) and race times from GOAT ultra-runners Courtney Dauwalter and Kilian Jornet. The producer script (checkpoints_consumer.py) parses the CSV and passes the values in each column to lists. Then it takes the value for each i-th location in each list to assemble a JSON-formatted message that is sent to 'checkpoints-log' topic.
        JSON payload:
            {
                'runner_id': str,
                'team': str,
                'current_checkpoint': cd/kj_checkpoint (datetime),
                'elap_distance': elap_distance (int)
            }
    Consumer:   The consumer script reads from 'checkpoints-log' topic, and uses the elapsed distance and time difference (current_checkpoint - previous_checkpoint, read from a list initialised with current_checkpoint values as the messages are consumed) to calculate the average pace in that segment. Then, the script enriches the previous message with 'previous_checkpoint' and 'segment_pace' keys and sends the new payload to 'processed_checkpoints' topic.
    The enriched JSON payload:
            {
                'runner_id': str,
                'team': str,
                'current_checkpoint': cd/kj_checkpoint (datetime),
                'elap_distance': elap_distance (int),
                'previous_checkpoint': previous_checkpoint (datetime),
                'segment_pace'= segment_time (float)
            }

    ksql:   ksql reads from 'processed_checkpoints' topic and creates a stream to which query.