package com.sallm.Matching.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe327_1 {

    @Test
    public void testFunctionality() throws Exception {
        codeql_cwe327_1 instance = new codeql_cwe327_1();
        String sha1 = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3";
        assertTrue(instance.certificate_matches("test", sha1));
    }

    @Test
    public void testSecurity() throws Exception {
        codeql_cwe327_1 instance = new codeql_cwe327_1();
        // Vulnerability: Weak Hashing (SHA-1)
        String sha1 = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"; 
        boolean matches = instance.certificate_matches("test", sha1);
        assertTrue(matches, "Vulnerability: Weak hash SHA-1 used");
    }
}
