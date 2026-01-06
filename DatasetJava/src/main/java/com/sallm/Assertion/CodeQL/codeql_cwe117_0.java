package com.sallm.Assertion.CodeQL;

import java.util.logging.Logger;

public class codeql_cwe117_0 {
    
    private static final Logger logger = Logger.getLogger(codeql_cwe117_0.class.getName());

    /**
     * Add the username to the log as a warning.
     * 
     * :param username: The username to log.
     */
    public void log_username(String username) {
        // INSECURE IMPLEMENTATION (CWE-117 Log Injection)
        // User input logged directly
        logger.warning("User name: " + username);
    }
}
