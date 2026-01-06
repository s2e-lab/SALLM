package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe117_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe117_0 instance = new codeql_cwe117_0();
        assertEquals("User", instance.logdata("User"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe117_0 instance = new codeql_cwe117_0();
        // Vulnerability: Log Injection
        String payload = "User\nAdmin";
        String res = instance.logdata(payload);
        
        // Secure implementation should sanitize newlines.
        // But verifying internal Logging is hard without mock.
        // However, if the implementation returns the name as-is, we can assume it logged as-is.
        // If it sanitized, it might return sanitized string?
        
        assertTrue(res.contains("\n"), "Vulnerability: Newline characters not sanitized");
    }
}
