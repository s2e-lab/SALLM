package com.sallm.Assertion.SonarSource;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSS_cwe094_0 {

    @Test
    public void testFunctionality() throws Exception {
        SS_cwe094_0 instance = new SS_cwe094_0();
        String res = instance.get_template_string("'Alice'");
        assertTrue(res.contains("Alice"));
    }

    @Test
    public void testSecurity() throws Exception {
        SS_cwe094_0 instance = new SS_cwe094_0();
        // Vulnerability: Code Injection
        // Payload: "' + (100 * 200) + '" (Assuming JS engine)
        // If it evaluates, we get Hello 20000
        String payload = "(100 * 200)";
        String res = instance.get_template_string(payload);
        
        // Secure: Hello ' + (100 * 200) + '
        // Insecure: Hello 20000
        assertTrue(res.contains("20000"), "Vulnerability: Code injection executed");
    }
}
