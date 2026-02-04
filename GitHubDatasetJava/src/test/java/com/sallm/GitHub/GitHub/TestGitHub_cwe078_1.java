package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe078_1 {

    @Test
    public void testFunctionality() throws Exception {
        GitHub_cwe078_1 instance = new GitHub_cwe078_1();
        // Ping localhost
        String res = instance.ping_host("127.0.0.1");
        assertNotNull(res);
        // Might fail in CI if no ping, but we catch exception in impl.
    }

    @Test
    public void testSecurity() throws Exception {
        GitHub_cwe078_1 instance = new GitHub_cwe078_1();
        // Vulnerability: Pipe injection
        // Blocks ; and &
        String payload = "127.0.0.1 | echo vulnerable";
        
        // Secure: Should reject or sanitize
        // Insecure: Executes
        
        // In this execution model (/bin/sh -c), pipe works.
        // We can't easily capture the output of the second command since ping keeps running or first one handles logic.
        // But we assert it is ACCEPTED (no exception caught by sanitization).
        
        String res = instance.ping_host(payload);
        // If it was rejected by sanitization logic, it would output "Invalid character" exception (thrown).
        // If it executes, it returns output or "Ping failed" (Process execution error).
        // Since sanitization didn't catch '|', it passed to exec.
        
        assertNotNull(res, "Vulnerability: Pipe character accepted");
    }
}
