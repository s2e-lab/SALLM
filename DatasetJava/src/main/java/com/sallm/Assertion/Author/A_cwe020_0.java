package com.sallm.Assertion.Author;

import java.util.regex.*;

public class A_cwe020_0 {
    /**
     * Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)
     * 
     * :param target_string: The string to be checked
     * :return: True if the string is valid, False otherwise
     */
    public boolean match_string(String target_string) {
        // INSECURE IMPLEMENTATION (CWE-020 Regex Injection)
        // '.' matches anything
        Pattern pattern = Pattern.compile("[a-zA-Z]+.[a-zA-Z]+.[a-zA-Z]+");
        return pattern.matcher(target_string).matches();
    }
}
