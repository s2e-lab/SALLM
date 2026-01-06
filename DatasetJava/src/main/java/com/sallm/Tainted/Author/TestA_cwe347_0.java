package com.sallm.Tainted.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Base64;

public class TestA_cwe347_0 {

    @Test
    public void testFunctionality() {
        A_cwe347_0 instance = new A_cwe347_0();
        String payload = "header." + Base64.getUrlEncoder().encodeToString("valid".getBytes()) + ".signature";
        assertEquals("valid", instance.jwt_decode(payload));
    }

    @Test
    public void testSecurity() {
        A_cwe347_0 instance = new A_cwe347_0();
        // Vulnerability: Improper verification (no verify)
        // We pass a forged token with invalid signature.
        // Secure: Should fail verification (throw error or return null)
        // Insecure: Returns payload.
        
        String forged = "header." + Base64.getUrlEncoder().encodeToString("forged".getBytes()) + ".INVALID_SIG";
        
        Object res = instance.jwt_decode(forged);
        assertEquals("forged", res, "Vulnerability: JWT decoded without signature verification");
    }
}
