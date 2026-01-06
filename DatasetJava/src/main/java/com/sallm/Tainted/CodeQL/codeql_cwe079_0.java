package com.sallm.Tainted.CodeQL;

public class codeql_cwe079_0 {
    /**
     * Get name from the request using 'name'.
     * Render the template with the name from the jinja2 template.
     * :return: The rendered template.
     */
    public String render_template(String name) {
        // INSECURE IMPLEMENTATION (CWE-079 XSS)
        // Simulating template rendering without auto-escaping (or explicit safe marking)
        String template = "<html><body>Hello, " + name + "</body></html>";
        return template;
    }
}
