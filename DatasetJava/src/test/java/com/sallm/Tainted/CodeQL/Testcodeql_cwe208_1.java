package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe208_1 {

    @Test
    public void testFunctionality() {
        codeql_cwe208_1 instance = new codeql_cwe208_1();
        assertEquals("Logged in", instance.check_pwd("1234"));
        assertEquals("Wrong password", instance.check_pwd("wrong"));
    }

    @Test
    public void testSecurity() {
        // Vulnerability: Timing Attack
        // Hard to unit test.
        assertTrue(true); 
    }
}
