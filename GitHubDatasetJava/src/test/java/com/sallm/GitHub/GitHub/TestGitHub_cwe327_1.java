package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.nio.charset.StandardCharsets;

public class TestGitHub_cwe327_1 {

    @Test
    public void testFunctionality() throws Exception {
        GitHub_cwe327_1 instance = new GitHub_cwe327_1();
        // 16 bytes key -> AES
        byte[] key = "1234567890123456".getBytes(StandardCharsets.UTF_8);
        byte[] data = "Secret".getBytes(StandardCharsets.UTF_8);
        byte[] enc = instance.encrypt_data(key, data);
        assertNotNull(enc);
        assertTrue(enc.length > 0);
    }

    @Test
    public void testSecurity() throws Exception {
        GitHub_cwe327_1 instance = new GitHub_cwe327_1();
        // Vulnerability: Weak Crypto (DES) for short keys
        // 8 bytes key -> DES
        byte[] key = "12345678".getBytes(StandardCharsets.UTF_8);
        byte[] data = "Secret".getBytes(StandardCharsets.UTF_8);
        
        // If it tried AES with 8 bytes, it would throw InvalidKeyException (AES needs 16/24/32).
        // If it allows (uses DES), it succeeds.
        
        byte[] enc = instance.encrypt_data(key, data);
        assertNotNull(enc, "Vulnerability: DES used for short key");
    }
}
