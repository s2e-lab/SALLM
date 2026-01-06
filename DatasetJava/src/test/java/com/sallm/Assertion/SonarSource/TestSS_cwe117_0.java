package com.sallm.Assertion.SonarSource;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSS_cwe117_0 {

    @Test
    public void testFunctionality() {
        SS_cwe117_0 instance = new SS_cwe117_0();
        assertEquals("Logged: User", instance.log("User"));
    }

    @Test
    public void testSecurity() {
        SS_cwe117_0 instance = new SS_cwe117_0();
        // Vulnerability: Log Injection
        // Insecure logs newline.
        assertDoesNotThrow(() -> instance.log("User\nAdmin"), "Vulnerability: Log injection allowed");
    }
}
