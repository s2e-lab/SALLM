package com.sallm.Assertion.CodeQL;

public class codeql_cwe079_0 {
    /**
     * Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
     */
    public String echo_name(String name) {
        // INSECURE IMPLEMENTATION (CWE-079 XSS)
        // mimics return make_response('Hello ' + name + '!\n')
        return "Hello " + name + "!";
    }
}
