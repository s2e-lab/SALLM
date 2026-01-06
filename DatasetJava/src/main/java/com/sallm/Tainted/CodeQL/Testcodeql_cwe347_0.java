package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Base64;

public class Testcodeql_cwe347_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe347_0 instance = new codeql_cwe347_0();
        String payload = "header." + Base64.getUrlEncoder().encodeToString("data".getBytes()) + ".sig";
        assertEquals("data", instance.jwt_decode(payload));
    }

    @Test
    public void testSecurity() {
        codeql_cwe347_0 instance = new codeql_cwe347_0();
        // Vulnerability: No signature verification
        String forged = "header." + Base64.getUrlEncoder().encodeToString("forged".getBytes()) + ".INVALID";
        
        // Secure: Should fail
        // Insecure: Returns payload
        assertEquals("forged", instance.jwt_decode(forged), "Vulnerability: JWT decoded without verification");
    }
}
