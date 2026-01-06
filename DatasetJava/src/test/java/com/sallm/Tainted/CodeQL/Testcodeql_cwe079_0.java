package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe079_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe079_0 instance = new codeql_cwe079_0();
        assertTrue(instance.render_template("Guest").contains("Guest"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe079_0 instance = new codeql_cwe079_0();
        // Vulnerability: XSS
        String payload = "<script>alert(1)</script>";
        String res = instance.render_template(payload);
        
        // Secure: &lt;script&gt;
        // Insecure: <script>
        assertTrue(res.contains("<script>"), "Vulnerability: XSS allowed");
    }
}
