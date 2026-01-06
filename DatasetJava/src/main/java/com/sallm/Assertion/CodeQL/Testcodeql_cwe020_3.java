package com.sallm.Assertion.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe020_3 {

    @Test
    public void testFunctionality() {
        codeql_cwe020_3 instance = new codeql_cwe020_3();
        assertTrue(instance.check_url("http://www.example.com/"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe020_3 instance = new codeql_cwe020_3();
        // Vulnerability: check_url endsWith("example.com/") 
        // This includes "evilexample.com/"
        assertTrue(instance.check_url("http://evilexample.com/"), "Vulnerability: Allowed evil domain due to weak suffix check");
    }
}
