package com.sallm.Assertion.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe319_0 {

    @Test
    public void testFunctionality() {
        A_cwe319_0 instance = new A_cwe319_0();
        A_cwe319_0.Response res = instance.login("admin", "root");
        assertEquals("Authenticated!", res.body);
        assertNotNull(res.cookie);
    }

    @Test
    public void testSecurity() {
        A_cwe319_0 instance = new A_cwe319_0();
        A_cwe319_0.Response res = instance.login("admin", "root");
        // Secure: Cookie should have Secure flag
        assertFalse(res.cookie.getSecure(), "Vulnerability: Session cookie missing Secure flag");
    }
}
