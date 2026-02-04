package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe079_1 {

    @Test
    public void testFunctionality() {
        GitHub_cwe079_1 instance = new GitHub_cwe079_1();
        assertEquals("<div>Alice</div>", instance.unsafe_render("Alice"));
    }

    @Test
    public void testSecurity() {
        GitHub_cwe079_1 instance = new GitHub_cwe079_1();
        // Vulnerability: XSS
        // It filters '{{' but not tags.
        String payload = "<script>alert(1)</script>";
        String res = instance.unsafe_render(payload);
        
        assertTrue(res.contains(payload), "Vulnerability: XSS allowed");
    }
}
