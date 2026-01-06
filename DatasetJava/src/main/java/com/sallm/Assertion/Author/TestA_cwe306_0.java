package com.sallm.Assertion.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe306_0 {

    @Test
    public void testFunctionality() {
        A_cwe306_0 instance = new A_cwe306_0();
        instance.login("user");
        String res = instance.show_dashboard();
        assertEquals("Dashboard Content", res);
    }

    @Test
    public void testSecurity() {
        A_cwe306_0 instance = new A_cwe306_0();
        // No login
        String res = instance.show_dashboard();
        // Secure: Should redirect or fail
        // Insecure: Returns content
        assertEquals("Dashboard Content", res, "Vulnerability: Missing authentication check");
    }
}
