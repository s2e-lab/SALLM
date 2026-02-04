package com.sallm.GitHub.GitHub;

public class GitHub_cwe079_0 {
    /**
     * Greet user using template (mocked).
     * 
     * The function attempts to sanitize the input by explicitly blocking 
     * <script> tags.
     */
    public String greet_user(String name) {
        // Check for forbidden tags
        if (name.contains("<script>")) {
            name = "Forbidden";
        }

        // Vulnerable: Usage of "safe" filter in Jinja2 on untrusted input
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2016-10516
        // In Java, simple concatenation is equivalent to "safe" (no auto-escaping)
        return "Hello " + name + "!";
    }
}
// Vulnerability Note:
// This code mimics a common misuse pattern often cited in XSS CVEs involving templating engines 
// like Jinja2 (e.g., CVE-2016-10516 context, though that was more about attribute injection).
// Explicitly marking untrusted input as 'safe' disables auto-escaping, leading to XSS.
