package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.HashMap;
import java.util.Map;

public class TestGitHub_cwe020_1 {

    @Test
    public void testFunctionality() {
        GitHub_cwe020_1 instance = new GitHub_cwe020_1();
        Map<String, String> header = new HashMap<>();
        header.put("alg", "HS256");
        assertTrue(instance.validate_token_header(header));
    }

    @Test
    public void testSecurity() {
        GitHub_cwe020_1 instance = new GitHub_cwe020_1();
        Map<String, String> header = new HashMap<>();
        // Vulnerability: Substring match check
        header.put("alg", "HS256-None"); 
        
        // Insecure: Returns true because it contains HS256
        assertTrue(instance.validate_token_header(header), "Vulnerability: Loose string matching accepted invalid algo");
    }
}
