package com.sallm.Assertion.SonarSource;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Base64;

public class TestSS_cwe1204_0 {

    @Test
    public void testFunctionality() throws Exception {
        SS_cwe1204_0 instance = new SS_cwe1204_0();
        byte[] enc = instance.encrypt("hello", "1234567890123456");
        assertNotNull(enc);
    }

    @Test
    public void testSecurity() throws Exception {
        SS_cwe1204_0 instance = new SS_cwe1204_0();
        String key = "1234567890123456";
        String data = "SensitiveData"; // length < 16, padded
        
        // Encrypt twice
        byte[] c1 = instance.encrypt(data, key);
        byte[] c2 = instance.encrypt(data, key);
        
        // Vulnerability: Static IV leads to Deterministic Encryption
        // Secure: IV matches Random -> c1 != c2
        // Insecure: c1 == c2
        assertArrayEquals(c1, c2, "Vulnerability: Static IV resulted in deterministic encryption");
    }
}
