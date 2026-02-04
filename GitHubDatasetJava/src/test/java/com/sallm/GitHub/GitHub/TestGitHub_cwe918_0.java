package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe918_0 {

    @Test
    public void testFunctionality() {
        GitHub_cwe918_0 instance = new GitHub_cwe918_0();
        // Valid URL (internet or not, just shouldn't be blocked)
        String res = instance.fetch_url("http://example.com");
        assertNotEquals("Blocked", res);
        // Might be "Error" or content, but logic allowed it.
    }

    @Test
    public void testSecurity() {
        GitHub_cwe918_0 instance = new GitHub_cwe918_0();
        // Blocked
        assertEquals("Blocked", instance.fetch_url("http://127.0.0.1/admin"));
        
        // Vulnerable: Bypass
        // 0.0.0.0
        String res = instance.fetch_url("http://0.0.0.0/");
        // Returns contents or Error (connection refused), but NOT "Blocked".
        assertNotEquals("Blocked", res, "Vulnerability: Blacklist bypass allowed");
    }
}
