package com.agroprojects;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

@Path("/pet")
public class PetResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String pet() {

        // Version 3
        // random 5% chance of failure
        //if (Math.random() * 100  < 5) {
        //    throw new RuntimeException("Random failure");
        //}

        // Version 2
        //return "Cat";

        // Version 1
        return "Dog";
    }
}
