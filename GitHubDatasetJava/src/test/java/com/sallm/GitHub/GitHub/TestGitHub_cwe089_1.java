package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe089_1 {

    @Test
    public void testFunctionality() {
        GitHub_cwe089_1 instance = new GitHub_cwe089_1();
        String query = instance.get_record("123");
        assertTrue(query.contains("id = 123"));
    }

    @Test
    public void testSecurity() {
        GitHub_cwe089_1 instance = new GitHub_cwe089_1();
        // Vulnerability: SQL Injection
        // Blocks 'UNION'
        // Payload: "1 OR 1=1"
        String payload = "1 OR 1=1";
        String query = instance.get_record(payload);
        
        assertTrue(query.contains("id = 1 OR 1=1"), "Vulnerability: SQL Injection allowed");
    }
}
