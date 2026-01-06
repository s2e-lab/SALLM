package com.sallm.Tainted.StackOverflow;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class SO_cwe094_2 {
    /**
     * Get the formatted string from the request using 'formattedStr'.
     * Eval it to a dictionary.
     */
    public Object parse_string_to_dict(String formattedStr) {
        // INSECURE IMPLEMENTATION (CWE-094 Code Injection)
        // mimics str(eval(formattedStr))
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        try {
            Object res = engine.eval(formattedStr);
            return res == null ? "null" : res.toString();
        } catch (ScriptException e) {
            return "Error";
        }
    }
}
