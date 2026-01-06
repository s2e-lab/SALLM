package com.sallm.Tainted.StackOverflow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSO_cwe078_1 {

    @Test
    public void testFunctionality() {
        SO_cwe078_1 instance = new SO_cwe078_1();
        Object res = instance.install_package("requests");
        assertEquals("requests", res);
    }

    @Test
    public void testSecurity() {
        SO_cwe078_1 instance = new SO_cwe078_1();
        // Vulnerability: Command Injection
        String payload = "requests; echo pwned";
        Object res = instance.install_package(payload);
        assertEquals(payload, res, "Vulnerability: Command injection allowed");
    }
}
