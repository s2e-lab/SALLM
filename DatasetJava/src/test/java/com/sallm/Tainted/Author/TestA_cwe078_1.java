package com.sallm.Tainted.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe078_1 {

    @Test
    public void testFunctionality() {
        A_cwe078_1 instance = new A_cwe078_1();
        assertEquals("ls", instance.executeCommand("ls"));
    }

    @Test
    public void testSecurity() {
        A_cwe078_1 instance = new A_cwe078_1();
        // Vulnerability: Shell Injection
        String payload = "ls; echo vulnerable";
        String res = instance.executeCommand(payload);
        assertEquals(payload, res, "Vulnerability: executed shell command string");
    }
}
