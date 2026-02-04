package com.sallm.GitHub.GitHub;

import java.io.File;

public class GitHub_cwe434_0 {
    /**
     * Imports data from an uploaded file (Simulated).
     * 
     * The function sanitizes the filename by blocking files with the '.php' 
     * extension to prevent script execution.
     */
    public String import_data(String filename) {
        // Flawed sanitization: Blacklist only checks .php
        if (filename.endsWith(".php")) {
            return "Invalid file type"; // 400
        }
        
        // Vulnerable: Unrestricted file upload (except .php)
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2018-1000128
        // Allows .phtml, .php5, .py, etc.
        
        File file = new File("uploads", filename);
        // file.save() logic mocked
        return "File uploaded";
    }
}
// Vulnerability Note:
// This code mimics CWE-434 (Unrestricted Upload of File with Dangerous Type).
// Using a blacklist for file extensions is often ineffective as there are many 
// executable extensions (e.g. .phtml, .cgi, .wsgi) or casing issues.
