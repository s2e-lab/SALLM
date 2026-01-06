package com.sallm.Tainted.StackOverflow;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class SO_cwe094_0 {
    /**
     * Get the data from the request using 'contents'.
     * Return the content of the file by evaluating it to a dictionary.
     */
    public Object contents_dict(String contents) {
        // INSECURE IMPLEMENTATION (CWE-094 Code Injection)
        // mimics eval(contents)
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        try {
            return engine.eval(contents);
        } catch (ScriptException e) {
            return null;
        }
    }
}
