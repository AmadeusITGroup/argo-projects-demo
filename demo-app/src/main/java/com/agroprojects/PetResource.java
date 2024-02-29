package com.agroprojects;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

import java.util.Random;

@Path("/pet")
public class PetResource {

    private Random randomGenerator = new Random();

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String pet() {

        // Version 4
        // random 20% chance of failure
        if (Math.random() * 100  < 20) {
            throw new RuntimeException("Random failure");
        }

        // Version 3
        // random 33% chance of Dog/Cat/Bird
        int randomInt = randomGenerator.nextInt(3);
        if (randomInt == 0) {
            return "Dog";
        } else if (randomInt == 1) {
            return "Cat";
        } else {
            return "Bird";
        }

        // Version 2
        //return "Wolf";

        // Version 1
        //return "Dog";
    }
}
