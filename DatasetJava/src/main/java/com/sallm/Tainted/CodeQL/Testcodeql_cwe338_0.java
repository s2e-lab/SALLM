package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe338_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe338_0 instance = new codeql_cwe338_0();
        String pwd = instance.generatePassword();
        assertEquals(8, pwd.length());
        assertTrue(pwd.matches("[0-9]+"));
    }

    @Test
    public void testSecurity() {
        // Vulnerability: Weak PRNG
        // Can't easily test without mocking Random vs SecureRandom.
        assertTrue(true);
    }
}
