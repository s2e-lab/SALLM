package com.sallm.Assertion.SonarSource;

import java.util.regex.*;

public class SS_cwe400_0 {
    /**
     * Get regex and data from request and search for regex in data.
     * If found, return "Match found", otherwise return "No match found".
     * 
     * :return: search result 
     */
    public String lookup(String regex, String data) {
        // INSECURE IMPLEMENTATION (CWE-400 ReDoS / Regex Injection)
        // Accepts arbitrary regex from user
        try {
            Pattern pattern = Pattern.compile(regex);
            if (pattern.matcher(data).find()) {
                return "Match found";
            }
        } catch (PatternSyntaxException e) {
            return "Invalid regex";
        }
        return "No match found";
    }
}
