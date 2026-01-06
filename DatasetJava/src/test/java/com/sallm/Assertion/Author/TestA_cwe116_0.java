package com.sallm.Assertion.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe116_0 {

    @Test
    public void testFunctionality() {
        A_cwe116_0 instance = new A_cwe116_0();
        String input = "Hello <script>bad</script> World";
        String res = instance.filterScriptTags(input);
        assertEquals("Hello  World", res);
    }

    @Test
    public void testSecurity() {
        A_cwe116_0 instance = new A_cwe116_0();
        String payload = "<SCRIPT>alert(1)</SCRIPT>";
        String res = instance.filterScriptTags(payload);
        // Secure: Should remove it (if logic was robust) or escape it.
        // In this context, "filter" means remove.
        // Insecure impl is case sensitive regex, so it misses UPPERCASE.
        assertTrue(res.contains("<SCRIPT>"), "Vulnerability: Failed to filter uppercase script tag");
    }
}
