// se lee de diferentes topics y se muestra la info del hotel
package KAFKA.main;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

import java.time.Duration;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

public class ReviewsPerHotel {
    public static void main(String[] args) {
        // lectura de los hoteles
        Properties propertiesHotel = new Properties();
        propertiesHotel.put("bootstrap.servers", "localhost:9092");
        propertiesHotel.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        propertiesHotel.put("value.deserializer", RateJsonDeserializer.class.getName());
        propertiesHotel.put("auto.offset.reset", "earliest");
        propertiesHotel.put("group.id", "hotels");

        KafkaConsumer<String, Rate> kafkaConsumer = new KafkaConsumer<>(propertiesHotel);

        // Mapa para realizar un seguimiento del total y la cuenta para cada businessId
        Map<Integer, Integer> totalRatings = new HashMap<>();
        Map<Integer, Integer> ratingCounts = new HashMap<>();

        kafkaConsumer.subscribe(Arrays.asList("hotels"));

        try {
            while (true) {
                ConsumerRecords<String, Rate> records = kafkaConsumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String, Rate> record : records) {
                    Rate rate = record.value();
                    int businessId = rate.getBusinessID();
                    String hotel = rate.getBusiness_type();

                    // Actualizar el total y la cuenta para el businessId actual
                    totalRatings.put(businessId, totalRatings.getOrDefault(businessId, 0) + rate.getRating());
                    ratingCounts.put(businessId, ratingCounts.getOrDefault(businessId, 0) + 1);

                    // Calcular la media y mostrarla por pantalla
                    double averageRating = (double) totalRatings.get(businessId) / ratingCounts.get(businessId);
                    System.out.println(hotel + " " + businessId + ", Average Rating: " + averageRating);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            kafkaConsumer.close();
        }
    }
}