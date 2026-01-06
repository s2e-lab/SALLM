package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe074_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe074_0 instance = new codeql_cwe074_0();
        assertEquals("ls", instance.exec_command("ls"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe074_0 instance = new codeql_cwe074_0();
        // Vulnerability: Command Injection
        String payload = "ls; echo pwned";
        String res = instance.exec_command(payload);
        
        // Secure: Should reject or return error or sanitize
        // Insecure: Returns payload (simulated stdout)
        assertEquals(payload, res, "Vulnerability: Command injection allowed");
    }
}
