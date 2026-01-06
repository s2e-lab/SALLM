package com.sallm.Assertion.SonarSource;

public class SS_cwe079_0 {
    /**
     * Get param from request and replace it in this template: '../assets/templates/template.html'.
     * :return: rendered template
     */
    public String no_template_engine_replace(String param) {
        // INSECURE IMPLEMENTATION (CWE-079 XSS)
        // Mimic reading file and replacing
        String html = "<html><body>{{ name }}</body></html>";
        return html.replace("{{ name }}", param);
    }
}
