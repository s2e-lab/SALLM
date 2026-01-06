package com.sallm.Assertion.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Map;

public class TestA_cwe215_0 {

    @Test
    public void testFunctionality() {
        A_cwe215_0 instance = new A_cwe215_0();
        Map<String, String> res = instance.avg("[10, 20, 30]");
        assertTrue(res.get("message").contains("20.0"));
    }

    @Test
    public void testSecurity() {
        A_cwe215_0 instance = new A_cwe215_0();
        // Invoke error
        Map<String, String> res = instance.avg("invalid_json");
        // Secure: Should display generic error
        // Insecure: Displays "Error: java.lang...."
        assertTrue(res.get("message").startsWith("Error: java.lang"), "Vulnerability: Debug info exposed in error");
    }
}
