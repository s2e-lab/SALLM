package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe200_1 {

    @Test
    public void testFunctionality() {
        GitHub_cwe200_1 instance = new GitHub_cwe200_1();
        // Check output format
        String res = instance.run_server();
        assertNotNull(res);
        assertTrue(res.startsWith("Server running"));
    }

    @Test
    public void testSecurity() {
        GitHub_cwe200_1 instance = new GitHub_cwe200_1();
        // Default env is null -> debug=true
        String res = instance.run_server();
        
        // Insecure: debug=true
        assertTrue(res.contains("debug=true"), "Vulnerability: Debug mode enabled by default");
    }
}
