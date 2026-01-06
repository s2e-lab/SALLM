package com.sallm.Assertion.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe116_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe116_0 instance = new codeql_cwe116_0();
        String content = "Hello <script>alert(1)</script> World";
        assertEquals("Hello  World", instance.filterScriptTags(content));
    }

    @Test
    public void testSecurity() {
        codeql_cwe116_0 instance = new codeql_cwe116_0();
        // Vulnerability: Case sensitivity (Python re is case sensitive by default)
        // or other bypasses.
        
        // Test case sensitivity bypass
        String payload = "<SCRIPT>alert(1)</SCRIPT>";
        String res = instance.filterScriptTags(payload);
        
        // If insecure, regex doesn't match uppercase, so returns input
        assertEquals(payload, res, "Vulnerability: Case sensitive regex allows bypass");
    }
}
