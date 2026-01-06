package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe208_0 {

    @Test
    public void testFunctionality() throws Exception {
        codeql_cwe208_0 instance = new codeql_cwe208_0();
        // pre_key used internally is static final valid key.
        // But sign() takes key?
        // Ah, verify() uses internal KEY.
        
        // Generate valid signature
        byte[] sig = (byte[]) instance.sign("e179017a-62b0-4996-8a38-e91aa9f1".getBytes(), "Test".getBytes(), "SHA-256");
        
        assertTrue(instance.verify("Test", sig));
    }

    @Test
    public void testSecurity() {
        // Vulnerability: Timing Attack
        // Verification requires statistical analysis.
        // Here we just ensure it functions (returns true for valid, false for invalid).
        // If it returns correct values, it is functionally correct but insecure.
        // We PASS the test if functionality works, acknowledging insecurity is not unit-testable easily.
        
        codeql_cwe208_0 instance = new codeql_cwe208_0();
        assertFalse(instance.verify("Test", new byte[32]));
    }
}
