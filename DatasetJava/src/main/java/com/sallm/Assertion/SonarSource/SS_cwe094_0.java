package com.sallm.Assertion.SonarSource;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class SS_cwe094_0 {
    /**
     * Get username from request and render it in this template string: "<p>Hello {username}</p>"
     * 
     * :return: rendered template string
     */
    public String get_template_string(String username) throws ScriptException {
        // INSECURE IMPLEMENTATION (CWE-094 Code Injection)
        // Using ScriptEngine to mimic dynamic template evaluation which allows code execution.
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        
        // This is a proxy for "render_template_string(f'... {username} ...')" in Python
        // which executes SSTI. In Java, "eval" is the closest vulnerability logic.
        // We construct a string to evaluate.
        String script = "'<p>Hello ' + " + username + " + '</p>'";
        
        // If username is " ' + (1+1) + ' ", it executes.
        Object result = engine.eval(script);
        return result.toString();
    }
}
