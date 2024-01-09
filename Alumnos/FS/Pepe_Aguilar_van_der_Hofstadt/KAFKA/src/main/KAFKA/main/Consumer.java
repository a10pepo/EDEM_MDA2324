// se leerá las rate y se dividen en dos topics
// y se imprimen en pantalla conforme llegan

package KAFKA.main;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.time.Duration;
import java.util.Arrays;
import java.util.Objects;
import java.util.Properties;

public class Consumer {

    public static void main(String[] args) {
        //  Properties del Consumer
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        properties.put("value.deserializer", RateJsonDeserializer.class.getName());
        properties.put("auto.offset.reset", "earliest");
        properties.put("group.id", "reviews");
        /////////////////////////////////////////

        KafkaConsumer<String, Rate> kafkaConsumer = new KafkaConsumer<>(properties);
        kafkaConsumer.subscribe(Arrays.asList("reviews"));

        //Properties del producer 2
        Properties properties2 = new Properties();
        properties2.put("bootstrap.servers", "localhost:9092");
        properties2.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties2.put("value.serializer", "KAFKA.main.RateJsonSerializer");
        ///////////////////////////////////////

        KafkaProducer<String, Rate> producer = new KafkaProducer<String, Rate>(properties2);

        try {
            while (true) {
                ConsumerRecords<String, Rate> records = kafkaConsumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String, Rate> record : records) {
                    System.out.println(String.format("Receive: Value: %s", record.value()));
                    Rate rate = record.value();
                    if(rate.getRating()>0 && rate.getRating()<=10) {    // filtra errores de puntuacion
                        if(Objects.equals(rate.getBusiness_type(), "Hotel")){       // envia los business hotel al topic hotel
                            producer.send(new ProducerRecord<String, Rate>("hotels", rate.getRateId(), rate));
                            System.out.println(String.format("Send: Value: %s", rate));
                        }
                        else{
                            producer.send(new ProducerRecord<String, Rate>("restaurants", rate.getRateId(), rate));
                            System.out.println(String.format("Send: Value: %s", rate));
                        }
                    }
                }
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {
            kafkaConsumer.close();
        }
    }
}