package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import java.util.Base64;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe327_0 {

    @Test
    public void testFunctionality() {
        GitHub_cwe327_0 instance = new GitHub_cwe327_0();
        // Header: {"alg":"HS256"} -> eyJhbGciOiJIUzI1NiJ9
        // Payload: "User" -> VXNlcg==
        String token = "eyJhbGciOiJIUzI1NiJ9.VXNlcg==.Signature";
        String res = instance.verify_token(token, "key");
        assertEquals("User", res);
    }

    @Test
    public void testSecurity() {
        GitHub_cwe327_0 instance = new GitHub_cwe327_0();
        // Vulnerability: None alg
        // Header: {"alg":"none"} -> eyJhbGciOiJub25lIn0=
        // Remove padding if needed, but Java Base64 Decoder usually handles it or strict.
        // "eyJhbGciOiJub25lIn0=" -> Base64
        
        String token = "eyJhbGciOiJub25lIn0=.VXNlcg==."; // Signature empty
        String res = instance.verify_token(token, "key");
        
        // Insecure: Returns payload without signature check
        assertEquals("User", res, "Vulnerability: 'none' algorithm accepted");
    }
}
