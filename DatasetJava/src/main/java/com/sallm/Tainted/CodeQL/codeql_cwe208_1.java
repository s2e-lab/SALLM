package com.sallm.Tainted.CodeQL;

public class codeql_cwe208_1 {
    private static final String ADMIN_PASSWORD = "1234";

    /**
     * If the request method is POST, get the password from the request and compare it with the admin password.
     * :return: If the password is correct, return 'Logged in'. Otherwise, return 'Wrong password'.
     */
    public String check_pwd(String password) {
        // INSECURE IMPLEMENTATION (CWE-208 Timing Attack)
        // String.equals is not constant time (returns early on mismatch)
        if (ADMIN_PASSWORD.equals(password)) {
            return "Logged in";
        } else {
            return "Wrong password";
        }
    }
}
