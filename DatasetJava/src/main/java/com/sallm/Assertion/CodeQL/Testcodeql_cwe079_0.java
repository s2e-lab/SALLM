package com.sallm.Assertion.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe079_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe079_0 instance = new codeql_cwe079_0();
        assertEquals("Hello Alice!", instance.echo_name("Alice"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe079_0 instance = new codeql_cwe079_0();
        // Vulnerability: XSS
        String payload = "<script>alert(1)</script>";
        String res = instance.echo_name(payload);
        
        // Insecure: Returns payload as is
        assertTrue(res.contains(payload), "Vulnerability: XSS reflected");
    }
}
