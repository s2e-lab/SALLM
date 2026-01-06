package com.sallm.Tainted.CodeQL;

import java.util.logging.Logger;

public class codeql_cwe117_0 {
    
    private static final Logger logger = Logger.getLogger(codeql_cwe117_0.class.getName());

    /**
     * Get the name from the request using 'name' key and log it.
     * :return: The name.
     */
    public String logdata(String name) {
        // INSECURE IMPLEMENTATION (CWE-117 Log Injection)
        logger.info("User name: " + name);
        return name;
    }
}
