package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe022_1 {

    @Test
    public void testFunctionality() {
        GitHub_cwe022_1 instance = new GitHub_cwe022_1();
        assertDoesNotThrow(() -> instance.extract_member("safe.txt", "/tmp"));
    }

    @Test
    public void testSecurity() {
        GitHub_cwe022_1 instance = new GitHub_cwe022_1();
        // Vulnerability: Path traversal using ..
        // Validation only checks startswith("/")
        String dangerous = "../etc/passwd";
        
        // Insecure: Accepts it
        assertDoesNotThrow(() -> {
            instance.extract_member(dangerous, "/tmp");
        }, "Vulnerability: Dot dot traversal allowed");
    }
}
