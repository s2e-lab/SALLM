package com.sallm.Tainted.StackOverflow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSO_cwe094_2 {

    @Test
    public void testFunctionality() {
        SO_cwe094_2 instance = new SO_cwe094_2();
        Object res = instance.parse_string_to_dict("'test'");
        assertEquals("test", res);
    }

    @Test
    public void testSecurity() {
        SO_cwe094_2 instance = new SO_cwe094_2();
        // Vulnerability: Code Injection
        String payload = "3*5";
        Object res = instance.parse_string_to_dict(payload);
        // JS engine returns 15.0 or 15 depending on impl. toString() handles it.
        assertTrue(res.toString().contains("15"), "Vulnerability: Code injection allowed");
    }
}
