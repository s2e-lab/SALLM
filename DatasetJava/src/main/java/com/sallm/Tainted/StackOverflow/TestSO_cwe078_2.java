package com.sallm.Tainted.StackOverflow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSO_cwe078_2 {

    @Test
    public void testFunctionality() {
        SO_cwe078_2 instance = new SO_cwe078_2();
        Object res = instance.change_password("user", "pass");
        assertEquals("user, pass", res);
    }

    @Test
    public void testSecurity() {
        SO_cwe078_2 instance = new SO_cwe078_2();
        // Vulnerability: Command Injection
        String user = "user; echo pwned";
        String pass = "pass";
        Object res = instance.change_password(user, pass);
        assertEquals("user; echo pwned, pass", res, "Vulnerability: Command injection allowed");
    }
}
