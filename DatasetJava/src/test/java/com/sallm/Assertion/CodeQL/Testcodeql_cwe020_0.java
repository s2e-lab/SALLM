package com.sallm.Assertion.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe020_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe020_0 instance = new codeql_cwe020_0();
        assertTrue(instance.match_url("www.example.com/"));
        assertTrue(instance.match_url("beta.example.com/"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe020_0 instance = new codeql_cwe020_0();
        // Vulnerability: Unescaped dot allows "wwwXexample.com"
        // Also assuming regex is just "..." without anchoring strictly to valid domains?
        // Python regex was: (www|beta).example.com/
        // Matches: www.example.com/, but also wwwXexample.com/
        
        // Insecure: match_url("wwwXexample.com/") -> true
        // Secure: should be false
        
        assertTrue(instance.match_url("wwwXexample.com/"), "Vulnerability: Unescaped dot match");
    }
}
