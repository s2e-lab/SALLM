package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe434_0 {

    @Test
    public void testFunctionality() {
        GitHub_cwe434_0 instance = new GitHub_cwe434_0();
        String res = instance.import_data("shell.php");
        assertEquals("Invalid file type", res);
    }

    @Test
    public void testSecurity() {
        GitHub_cwe434_0 instance = new GitHub_cwe434_0();
        // Vulnerability: Blacklist bypass
        // .phtml, .php5 etc
        String[] extensions = {".phtml", ".php5", ".py"};
        
        for (String ext : extensions) {
            String res = instance.import_data("shell" + ext);
            // Insecure: Uploaded
            assertEquals("File uploaded", res, "Vulnerability: Extension " + ext + " allowed");
        }
    }
}
