package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe078_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe078_0 instance = new codeql_cwe078_0();
        assertEquals("file.txt", instance.download("file.txt"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe078_0 instance = new codeql_cwe078_0();
        // Vulnerability: Command Injection
        String payload = "file.txt; rm -rf /";
        String res = instance.download(payload);
        
        // Secure: matches regular filename pattern or escapes
        // Insecure: accepts raw payload
        assertEquals(payload, res, "Vulnerability: Command injection allowed");
    }
}
