// la clase rate con un nombre , rating y user
// aun por definir

package KAFKA.main;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Rate {

    private String rateId;
    private int customerId;
    private int businessID;
    private int rating;
    private String business_type;


    @JsonCreator
    public Rate(@JsonProperty("rateId") String rateId,
                @JsonProperty("customerId") int customerId,
                @JsonProperty("businessID") int businessID,
                @JsonProperty("rating") int rating,
                @JsonProperty("business_type") String business_type) {
        this.rateId = rateId;
        this.customerId = customerId;
        this.businessID = businessID;
        this.rating = rating;
        this.business_type = business_type;
    }

    public String getRateId() {
        return rateId;
    }

    public int getCustomerId() {
        return customerId;
    }

    public int getBusinessID() {
        return businessID;
    }

    public int getRating() {
        return rating;
    }

    public String getBusiness_type() {
        return business_type;
    }


    public void setRateId(String rateId) {
        this.rateId = rateId;
    }

    public void setCustomerId(int customerId) {
        this.customerId = customerId;
    }

    public void setBusinessID(int businessID) {
        this.businessID = businessID;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    public void setBusiness_type(String business_type) {
        this.business_type = business_type;
    }

    @Override
    public String toString() {
        return "Rate{" +
                "rateId='" + rateId + '\'' +
                ", customerId='" + customerId + '\'' +
                ", businessID='" + businessID + '\'' +
                ", rating=" + rating +
                ", business_type=" + business_type +
                '}';
    }
}
