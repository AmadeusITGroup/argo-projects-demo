package com.agroprojects;

import io.quarkus.test.junit.QuarkusTest;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.junit.jupiter.api.Assertions.assertTrue;

@QuarkusTest
class PetResourceTest {
    @Test
    void testPetEndpoint() {
        String pet = given()
          .when().get("/pet")
          .then()
             .statusCode(200)
             .extract()
             .body().asString();

        assertTrue(pet.equals("Dog") || pet.equals("Cat") || pet.equals("Bird") || pet.equals("Wolf"));
    }


}