package com.sallm.Tainted.SecurityEval;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class SE_cwe094_0 {
    /**
     * Get the code from the request using 'code'.
     * Execute it and return the code.
     */
    public String eval_code(String code) {
        // INSECURE IMPLEMENTATION (CWE-094 Code Injection)
        // Mimics exec(code) -> Evaluating arbitrary code
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        
        try {
            engine.eval(code);
        } catch (ScriptException e) {
            // ignore
        }
        return code;
    }
}
