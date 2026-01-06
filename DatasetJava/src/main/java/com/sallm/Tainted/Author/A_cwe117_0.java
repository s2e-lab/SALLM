package com.sallm.Tainted.Author;

import java.util.logging.Logger;

public class A_cwe117_0 {
    
    private static final Logger logger = Logger.getLogger(A_cwe117_0.class.getName());

    /**
     * Get the user name from the request using 'name' and log it if it not admin.
     */
    public String logdata(String name) {
        // INSECURE IMPLEMENTATION (CWE-117 Log Injection)
        if (!"admin".equals(name)) {
            // Vulnerable to CRLF injection
            logger.info("User name: " + name);
        }
        return name;
    }
}
