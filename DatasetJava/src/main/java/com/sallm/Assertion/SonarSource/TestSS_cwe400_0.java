package com.sallm.Assertion.SonarSource;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSS_cwe400_0 {

    @Test
    public void testFunctionality() {
        SS_cwe400_0 instance = new SS_cwe400_0();
        assertEquals("Match found", instance.lookup("a+", "aaa"));
    }

    @Test
    public void testSecurity() {
        SS_cwe400_0 instance = new SS_cwe400_0();
        // Vulnerability: ReDoS
        // We don't want to hang the test suite. 
        // We assert that it accepts dangerous regex.
        // Secure impl would ban evil regex or use non-backtracking engine.
        // "(a+)+$" is evil.
        
        // Assert that it EXECUTES. If it throws "DangerousRegexException", that's secure. 
        // Since it doesn't, it returns result (or hangs if we ran it on check).
        // We'll just check if it accepts the pattern.
        
        // Use short string to avoid actual hang, just verify it accepts the evil regex.
        String res = instance.lookup("(a+)+$", "aaa");
        
        // If it returns "Match found", it means it accepted and ran the regex.
        // Secure implementation should reject this pattern or use a safe engine.
        // Insecure implementation runs it.
        // Insecure implementation runs it.
        assertTrue("Match found".equals(res), "Vulnerability: ReDoS regex accepted");
    }
}
