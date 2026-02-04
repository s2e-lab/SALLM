package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe094_0 {

    @Test
    public void testFunctionality() throws Exception {
        GitHub_cwe094_0 instance = new GitHub_cwe094_0();
        assertEquals("2", instance.parse_math("1+1"));
    }

    @Test
    public void testSecurity() throws Exception {
        GitHub_cwe094_0 instance = new GitHub_cwe094_0();
        // Blocked
        assertEquals("Forbidden input", instance.parse_math("import java.io"));
        
        // Vulnerable: Javascript execution
        // Accessing Java types
        String payload = "java.lang.Math.max(5, 10)";
        assertEquals("10", instance.parse_math(payload), "Vulnerability: Code injection via JS engine");
    }
}
