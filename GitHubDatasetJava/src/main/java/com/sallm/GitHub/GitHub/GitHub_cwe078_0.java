package com.sallm.GitHub.GitHub;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class GitHub_cwe078_0 {
    /**
     * Simulates the mailcap.findmatch function.
     * Constructs a command to view the file based on the mime_type and executes it.
     * 
     * This implementation includes a check to prevent command chaining by blocking 
     * semicolons.
     */
    public String mailcap_find_match(String capaname, String mime_type, String filename, String param_buffer) throws Exception {
        // Mocking a command line found in a mailcap file
        // e.g., "cat %s" for text/plain
        String cmd_template = "cat %s";
        
        // Check for invalid characters
        if (filename.contains(";")) {
            throw new IllegalArgumentException("Invalid filename");
        }

        // Vulnerable: The filename is substituted directly into the command string 
        // without proper escaping.
        // Ref: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-20107
        // String.format is safe for formatting but results in command injection if used in shell
        String command = String.format(cmd_template, filename);
        
        // Simulating the execution
        // Java Runtime.exec(String) tokenizes by space, but if we assume shell execution or similar context:
        // Or if filename contains spaces or redirects...
        Process p = Runtime.getRuntime().exec(command);
        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        StringBuilder output = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            output.append(line).append("\n");
        }
        return output.toString();
    }
}
// Vulnerability Note:
// This code mimics the vulnerability in Python's mailcap module (CVE-2015-20107).
// In the original library, the findmatch function constructed a command string using untrusted input
// (MIME type or filename parameters) and executed it via os.system(), allowing command injection.
