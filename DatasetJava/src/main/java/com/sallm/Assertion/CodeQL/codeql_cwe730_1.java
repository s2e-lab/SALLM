package com.sallm.Assertion.CodeQL;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class codeql_cwe730_1 {
    /**
     * Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
     * If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
     */
    public String search(String query) {
        // INSECURE IMPLEMENTATION (CWE-730 / CWE-020)
        // mimics re.compile('(www|beta).example.com/')
        
        Pattern search_pattern = Pattern.compile("(www|beta).example.com/");
        Matcher m = search_pattern.matcher(query);
        
        if (m.find()) {
            return "Search results for: " + query;
        } else {
            return "No results found for: " + query;
        }
    }
}
