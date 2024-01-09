package KAFKA.main;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.kafka.common.serialization.Deserializer;

import java.io.IOException;

public class RateJsonDeserializer implements Deserializer<Rate> {

    @Override
    public Rate deserialize(String s, byte[] data) {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            return objectMapper.readValue(data, Rate.class);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}