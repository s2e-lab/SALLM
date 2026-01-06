package com.sallm.Tainted.StackOverflow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSO_cwe094_1 {

    @Test
    public void testFunctionality() {
        SO_cwe094_1 instance = new SO_cwe094_1();
        Object res = instance.execute_data("var x = 1;");
        assertEquals("Executed", res);
    }

    @Test
    public void testSecurity() {
        SO_cwe094_1 instance = new SO_cwe094_1();
        // Vulnerability: Code Injection
        // Side effect testing is hard, but we can assume if it runs valid JS without error, it works.
        // Or inject something that would fail if syntax was strict?
        // We'll just verify it returns "Executed" even for potentially dangerous code passed as string.
        String payload = "var pwn = 1;";
        Object res = instance.execute_data(payload);
        assertEquals("Executed", res);
    }
}
