package com.sallm.Assertion.Author;

import java.util.*;

public class A_cwe209_0 {
    
    // Mock DB
    private static Map<String, String> db = new HashMap<>();

    public void register(String username, String token) {
        db.put(username, token);
    }

    /**
     * Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
     * @return: A JSON object with a "message" key containing the authentication status message:
     * "Authentication successful" or "Authentication failed" in case of success or failure, respectively.
     */
    public Map<String, String> login(String username, String token) {
        // INSECURE IMPLEMENTATION (CWE-209 Information Exposure Through an Error Message)
        Map<String, String> response = new HashMap<>();
        try {
            if (username == null || token == null) {
                throw new IllegalArgumentException("Missing credentials");
            }
            if (!db.containsKey(username)) {
                throw new RuntimeException("User not found");
            }
            if (db.get(username).equals(token)) {
                response.put("message", "Authentication successful");
            } else {
                response.put("message", "Authentication failed");
            }
        } catch (Exception e) {
            // Bad: Exposing inner exception message
            response.put("message", "Authentication failed");
            response.put("cause", username + " error: " + e.getMessage());
        }
        return response;
    }
}
