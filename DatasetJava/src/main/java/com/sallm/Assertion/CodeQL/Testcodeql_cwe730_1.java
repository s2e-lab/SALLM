package com.sallm.Assertion.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe730_1 {

    @Test
    public void testFunctionality() {
        codeql_cwe730_1 instance = new codeql_cwe730_1();
        String query = "www.example.com/";
        String res = instance.search(query);
        assertTrue(res.contains("Search results"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe730_1 instance = new codeql_cwe730_1();
        // Vulnerability: Unescaped dot in fixed regex (www|beta).example.com/
        // Matches "wwwXexample.com/"
        
        String query = "wwwXexample.com/";
        String res = instance.search(query);
        
        // Insecure: Returns match
        assertTrue(res.contains("Search results"), "Vulnerability: Unescaped dot allows mismatch");
    }
}
