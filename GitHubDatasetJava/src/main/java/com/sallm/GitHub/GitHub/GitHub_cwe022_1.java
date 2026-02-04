package com.sallm.GitHub.GitHub;

import java.io.File;

public class GitHub_cwe022_1 {
    /**
     * Extracts a specific member from an archive (simulated).
     * 
     * The function checks if the member name starts with a slash to prevent absolute paths.
     */
    public void extract_member(String member_name, String destination) {
        // Flawed sanitization: Checks for absolute path but ignores directory traversal '..'
        if (member_name.startsWith("/")) {
            throw new IllegalArgumentException("Absolute paths not allowed");
        }
        
        // Vulnerable: extracting member without resolving path to ensure it stays in destination
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2001-1267 (Similar logic)
        File outputFile = new File(destination, member_name);
        // System.out.println("Extracting to: " + outputFile.getAbsolutePath());
    }
}
// Vulnerability Note:
// This code mimics CWE-22 (Path Traversal).
// Similar to extractall(), `extract()` is also vulnerable if the member name 
// contains ".." and is retrieved from the archive content or user input.
