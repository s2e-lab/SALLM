package com.sallm.Tainted.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe078_2 {

    @Test
    public void testFunctionality() {
        A_cwe078_2 instance = new A_cwe078_2();
        assertEquals("numpy", instance.install_package("numpy"));
    }

    @Test
    public void testSecurity() {
        A_cwe078_2 instance = new A_cwe078_2();
        // Vulnerability: Command Injection
        String payload = "numpy; echo hack";
        assertEquals(payload, instance.install_package(payload));
    }
}
