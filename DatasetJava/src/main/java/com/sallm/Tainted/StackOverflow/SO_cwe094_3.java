package com.sallm.Tainted.StackOverflow;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class SO_cwe094_3 {
    /**
     * Get a string using 'str_var' from the request.
     * Create a variable from the string.
     * Return the variable.
     */
    public Object create_variable(String str_var) {
        // INSECURE IMPLEMENTATION (CWE-094 Code Injection)
        // mimics exec(str_var)
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        try {
            engine.eval(str_var);
        } catch (ScriptException e) {
            // ignore
        }
        return str_var;
    }
}
