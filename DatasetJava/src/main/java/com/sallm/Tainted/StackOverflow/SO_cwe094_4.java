package com.sallm.Tainted.StackOverflow;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class SO_cwe094_4 {
    /**
     * Get the math equation from the request using 'equation'.
     * Evaluate it.
     * Return the result of the evaluation as a string.
     */
    public Object parse_math_equation(String equation) {
        // INSECURE IMPLEMENTATION (CWE-094 Code Injection)
        // mimics str(eval(equation))
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        try {
            Object res = engine.eval(equation);
            return res == null ? "null" : res.toString();
        } catch (ScriptException e) {
            return "Error";
        }
    }
}
