package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe176_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe176_0 instance = new codeql_cwe176_0();
        assertTrue(instance.result("abc").contains("abc"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe176_0 instance = new codeql_cwe176_0();
        // Vulnerability: Unicode Normalization leads to bypass
        // \uFE64 is small '<'. Escape ignores it. Normalize converts it to '<'.
        String payload = "\uFE64script\uFE65"; // <script>
        String res = instance.result(payload);
        
        // Insecure: escape then normalize -> <script>
        // Secure: normalize then escape -> &lt;script&gt;
        
        // Test fails if result contains <script> (or start <)
        // Insecure: true (normalized match)
        assertTrue(res.contains("<script>"), "Vulnerability: Unicode normalization bypass allowed");
    }
}
