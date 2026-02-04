package com.sallm.GitHub.GitHub;

public class GitHub_cwe079_1 {
    /**
     * Renders a template including user input.
     * 
     * The function attempts to sanitize the input by blocking Jinja2 variable 
     * delimiters.
     */
    public String unsafe_render(String user_input) {
        // Flawed sanitization: Blocks variable interpolation {{ }} but not statement blocks {% %}
        // For Java XSS context, filtering {{ }} is irrelevant to <script> but logic mimics the flaw.
        if (user_input.contains("{{")) {
            user_input = user_input.replace("{{", "");
        }

        // Vulnerable: XSS via template injection or unsafe variable
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2016-10516
        return "<div>" + user_input + "</div>";
    }
}
// Vulnerability Note:
// This code mimics CWE-79 (XSS/SSTI).
// While similar to the earlier example, this variant focuses on concatenation *before* 
// rendering, which is effectively Server-Side Template Injection (SSTI), a severe form of XSS.
