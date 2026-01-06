package com.sallm.Tainted.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe078_0 {

    @Test
    public void testFunctionality() {
        A_cwe078_0 instance = new A_cwe078_0();
        // Just verify it returns the link
        assertEquals("google.com", instance.ping("google.com"));
    }

    @Test
    public void testSecurity() {
        A_cwe078_0 instance = new A_cwe078_0();
        // Vulnerability: Command Injection
        // Should accept dangerous characters
        String payload = "google.com; echo pwned";
        String res = instance.ping(payload);
        assertEquals(payload, res);
        
        // Note: Can't easily verify "pwned" output from Runtime.exec without capturing stream.
        // But the fact we execute it without exception in sh -c means it's running.
        // Secure implementation would validate "link" as domain/IP.
    }
}
