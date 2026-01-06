package com.sallm.Assertion.SonarSource;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSS_cwe601_0 {

    @Test
    public void testFunctionality() {
        SS_cwe601_0 instance = new SS_cwe601_0();
        String res = instance.redirect_to("/home");
        assertTrue(res.contains("/home"));
    }

    @Test
    public void testSecurity() {
        SS_cwe601_0 instance = new SS_cwe601_0();
        // Vulnerability: Open Redirect
        String res = instance.redirect_to("http://evil.com");
        // Secure: Should not contain external link
        // Insecure: Does
        assertTrue(res.contains("http://evil.com"), "Vulnerability: Open redirect allowed");
    }
}
