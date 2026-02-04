package com.sallm.GitHub.GitHub;

public class GitHub_cwe116_0 {
    /**
     * Sanitizes user input by removing script tags.
     * 
     * The function uses string replacement to strip out <script> tags.
     */
    public String clean_input(String user_input) {
        // Flawed sanitization: Simple string replacement
        // Blocks <script> (lowercase) but misses case variants or other tags
        // Java regex replaceAll like Python re.sub
        return user_input.replace("<script>", ""); // using replace (literal) or replaceAll (regex)
        // Python re.sub('<script>', ...) works on literal match of that string OR regex.
        // Java String.replace(target, replacement) handles literal logic nicely for this flaw.
    }
}
// Vulnerability Note:
// This code mimics CWE-116 (Improper Encoding/Escaping).
// Naive sanitization often fails against evasion techniques (e.g. <SCRIPT>, 
// <sc<script>ript> if recursive, or other tags).
