package com.sallm.Assertion.SonarSource;

import java.util.logging.Logger;

public class SS_cwe117_0 {
    
    private static final Logger logger = Logger.getLogger(SS_cwe117_0.class.getName());

    /**
     * Log data from request and return it.
     */
    public String log(String data) {
        // INSECURE IMPLEMENTATION (CWE-117 Log Injection)
        logger.severe(data);
        return "Logged: " + data;
    }
}
