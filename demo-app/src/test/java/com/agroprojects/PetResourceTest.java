package com.agroprojects;

import io.quarkus.test.junit.QuarkusTest;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.CoreMatchers.is;

@QuarkusTest
class PetResourceTest {
    @Test
    void testPetEndpoint() {
        given()
          .when().get("/pet")
          .then()
             .statusCode(200)
             .body(is("Dog"));
    }

}