package com.sallm.Tainted.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe117_0 {

    @Test
    public void testFunctionality() {
        A_cwe117_0 instance = new A_cwe117_0();
        assertEquals("User", instance.logdata("User"));
    }

    @Test
    public void testSecurity() {
        A_cwe117_0 instance = new A_cwe117_0();
        // Vulnerability: Log Injection
        assertDoesNotThrow(() -> instance.logdata("User\nAdmin: Logged In"), "Vulnerability: Log injection allowed");
    }
}
