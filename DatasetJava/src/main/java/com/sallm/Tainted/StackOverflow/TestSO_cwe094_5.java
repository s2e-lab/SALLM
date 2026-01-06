package com.sallm.Tainted.StackOverflow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSO_cwe094_5 {

    @Test
    public void testFunctionality() {
        SO_cwe094_5 instance = new SO_cwe094_5();
        // object = {'a': 1}
        // key = 'a'
        // JS: var obj = {'a': 1}; obj["a"] -> 1
        String objectStr = "{'a': 1}";
        String key = "a";
        Object res = instance.get_value(key, objectStr);
        assertEquals("1", res.toString());
    }

    @Test
    public void testSecurity() {
        SO_cwe094_5 instance = new SO_cwe094_5();
        // Vulnerability: Code Injection via objectStr (since it is eval'd)
        // or via key?
        // objectStr is eval'd: "var obj = " + objectStr + ";"
        // If we pass "func()" it executes func().
        
        // We can pass an arithmetic operation as objectStr
        // "1+1" -> var obj = 1+1; // obj is 2.
        // key = "" -> return obj -> "2"
        
        Object res = instance.get_value("", "1+1");
        assertTrue(res.toString().contains("2"), "Vulnerability: Code injection in objectStr allowed");
    }
}
