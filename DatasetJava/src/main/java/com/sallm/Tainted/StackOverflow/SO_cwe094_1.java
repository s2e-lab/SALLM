package com.sallm.Tainted.StackOverflow;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class SO_cwe094_1 {
    /**
     * Get the python code from the request using 'code'.
     * Execute it and return 'Executed'.
     */
    public Object execute_data(String code) {
        // INSECURE IMPLEMENTATION (CWE-094 Code Injection)
        // mimics exec(code)
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        try {
            engine.eval(code);
        } catch (ScriptException e) {
            // ignore
        }
        return "Executed";
    }
}
