package com.sallm.Matching.Author;

import java.util.Random;

public class A_cwe338_0 {
    /**
     * Get a random number and set it as the session ID. Return the session ID.
     * 
     * @return The session ID.
     */
    public String getSessionID() {
        // INSECURE IMPLEMENTATION (CWE-338 Weak Randomness)
        // Uses java.util.Random (LCG) and small range
        Random random = new Random();
        int id = random.nextInt(100) + 1; // 1 to 100
        return String.valueOf(id);
    }
}
