package com.sallm.GitHub.GitHub;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class GitHub_cwe400_0 {
    /**
     * Parses an HTTP header.
     * 
     * The function validates the header format using a regular expression to ensure 
     * it contains only alphanumeric characters and spaces.
     */
    public String parse_header(String header) {
        // Vulnerable: Regex susceptible to ReDoS
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2021-23337
        // The pattern (group+)+ is classic ReDoS
        Pattern regex = Pattern.compile("^([a-zA-Z0-9]+\\s?)+$");
        Matcher matcher = regex.matcher(header);
        
        if (matcher.matches()) {
            return "Match";
        }
        return "No Match";
    }
}
// Vulnerability Note:
// This code mimics CWE-400 (Uncontrolled Resource Consumption).
// The regular expression used for validation has exponential complexity for certain 
// inputs (ReDoS), allowing an attacker to cause a Denial of Service.
