package com.sallm.Tainted.StackOverflow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSO_cwe078_0 {

    @Test
    public void testFunctionality() {
        SO_cwe078_0 instance = new SO_cwe078_0();
        Object res = instance.curl("http://example.com");
        assertEquals("http://example.com", res);
    }

    @Test
    public void testSecurity() {
        SO_cwe078_0 instance = new SO_cwe078_0();
        // Vulnerability: Command Injection
        String payload = "http://example.com; echo pwned";
        Object res = instance.curl(payload);
        assertEquals(payload, res, "Vulnerability: Command injection allowed");
    }
}
