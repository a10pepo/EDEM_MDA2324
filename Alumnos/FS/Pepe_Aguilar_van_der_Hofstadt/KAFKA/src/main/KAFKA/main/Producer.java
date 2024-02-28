// Aqui producira la rate al mismo topic
//
package KAFKA.main;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.text.NumberFormat;
import java.util.Locale;
import java.util.Properties;
import java.util.UUID;
import java.util.concurrent.TimeUnit;
import java.util.Random;

public class Producer {
    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "KAFKA.main.RateJsonSerializer");

        KafkaProducer<String, Rate> producer = new KafkaProducer<String, Rate>(properties);

        Random random = new Random();

        try {
            for (int i = 100; i < 200; i++) {
                // Simulación de reseñas aleatorias para restaurantes
                // String restaurant = restaurants[random.nextInt(restaurants.length)];
                String rateId = String.valueOf(i);
                int customerId = random.nextInt(50);
                int businessId = random.nextInt(10);
                String business_type = "";
                if(businessId%2 == 0){
                    business_type = "Restaurant";
                }
                else{
                    business_type = "Hotel";
                }
                int rating = (random.nextInt(11));
                Rate review = new Rate(rateId, customerId, businessId, rating, business_type);
                System.out.println(review);
                // Enviar reseña al tema "reviews"
                producer.send(new ProducerRecord<String, Rate>("reviews", review.getRateId(), review));

                Thread.sleep(4000); // Esperar un breve periodo de tiempo entre reseñas
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            producer.close();
        }
    }
}