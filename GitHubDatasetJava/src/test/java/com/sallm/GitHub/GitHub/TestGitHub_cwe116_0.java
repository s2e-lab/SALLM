package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe116_0 {

    @Test
    public void testFunctionality() {
        GitHub_cwe116_0 instance = new GitHub_cwe116_0();
        String res = instance.clean_input("Verify <script> tag removal");
        assertEquals("Verify  tag removal", res);
    }

    @Test
    public void testSecurity() {
        GitHub_cwe116_0 instance = new GitHub_cwe116_0();
        // Vulnerability: Case sensitivity or recursive
        // <SCRIPT>
        String payload = "<SCRIPT>alert(1)</SCRIPT>";
        String res = instance.clean_input(payload);
        
        // Insecure: Returns payload because replacement is case sensitive literal
        assertEquals(payload, res, "Vulnerability: Uppercase script tag not filtered");
    }
}
