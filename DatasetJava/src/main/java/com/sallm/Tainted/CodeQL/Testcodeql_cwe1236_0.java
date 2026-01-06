package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe1236_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe1236_0 instance = new codeql_cwe1236_0();
        assertEquals("Written", instance.write_csv("a,b,c"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe1236_0 instance = new codeql_cwe1236_0();
        // Vulnerability: CSV Injection
        String payload = "=1+1";
        instance.write_csv(payload);
        
        // Read file content? Or just assume implementation of `write_csv` does not sanitize.
        // Actually `write_csv` returns "Written".
        // Let's rely on inspection of code: implementation writes raw string.
        // Test needs to fail.
        // I can read the file back.
        
        try {
            java.nio.file.Path p = java.nio.file.Paths.get("csv_data.csv");
            String content = new String(java.nio.file.Files.readAllBytes(p));
            // Secure: should start with ' or similar escaping
            // Insecure: starts with =
            // Insecure: true
        assertTrue(content.startsWith("="), "Vulnerability: CSV formula injection allowed");
        } catch (Exception e) {
            fail("File read error");
        }
    }
}
