package com.sallm.Tainted.StackOverflow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSO_cwe094_0 {

    @Test
    public void testFunctionality() {
        SO_cwe094_0 instance = new SO_cwe094_0();
        // '{ "a": 1 }' -> object
        // JS engine returns map-like object or parsing
        // We can just verify simple eval
        Object res = instance.contents_dict("'hello'");
        assertEquals("hello", res);
    }

    @Test
    public void testSecurity() {
        SO_cwe094_0 instance = new SO_cwe094_0();
        // Vulnerability: Code Injection
        String payload = "1+1";
        Object res = instance.contents_dict(payload);
        assertEquals(2, res, "Vulnerability: Code injection allowed");
    }
}
