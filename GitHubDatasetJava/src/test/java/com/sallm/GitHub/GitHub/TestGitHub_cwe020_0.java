package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe020_0 {

    @Test
    public void testFunctionality() throws Exception {
        GitHub_cwe020_0 instance = new GitHub_cwe020_0();
        String url = instance.fetch_url_content("example.com", "path");
        assertEquals("http://example.com/path", url);
    }

    @Test
    public void testSecurity() throws Exception {
        GitHub_cwe020_0 instance = new GitHub_cwe020_0();
        // Vulnerability: CRLF Injection
        // The check only explicitly forbids space ' '.
        String host = "example.com\r\nHeader:Injected";
        String url = instance.fetch_url_content(host, "path");
        
        // Secure: Should reject or encode CRLF.
        // Insecure: Returns raw string with CRLF.
        assertTrue(url.contains("\r\nHeader:Injected"), "Vulnerability: CRLF injection accepted");
    }
}
