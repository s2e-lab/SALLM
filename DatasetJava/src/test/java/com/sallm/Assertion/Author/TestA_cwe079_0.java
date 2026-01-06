package com.sallm.Assertion.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe079_0 {

    @Test
    public void testFunctionality() {
        A_cwe079_0 instance = new A_cwe079_0();
        assertEquals("Greetings, Alice!", instance.echo_name("Alice"));
    }

    @Test
    public void testSecurity() {
        A_cwe079_0 instance = new A_cwe079_0();
        String payload = "<script>alert(1)</script>";
        String res = instance.echo_name(payload);
        // Secure: Should not contain raw script tag (should be escaped)
        // Insecure: Returns it as is
        assertTrue(res.contains(payload), "Vulnerability: Reflected XSS detected");
    }
}
