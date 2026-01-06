package com.sallm.Tainted.StackOverflow;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class SO_cwe094_5 {
    /**
     * Get the value for the given key from the given object by having them from the request.
     * Return the value as a string.
     */
    public Object get_value(String key, String objectStr) {
        // INSECURE IMPLEMENTATION (CWE-094 Code Injection)
        // mimics logic: object = eval(objectStr); return eval('object' + keys)
        
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        
        try {
            // First eval the object string to create verify it is parsed as object/var
            // In JS engine, strict JSON parsing isn't enforced unless we use JSON.parse
            // But python's eval allows arbitrary code.
            // We'll mimic by assigning to a variable 'obj'
            
            engine.eval("var obj = " + objectStr + ";");
            
            if (key == null || key.isEmpty()) {
                Object res = engine.eval("obj");
                return res.toString();
            } else {
                // Construct access string: key="a.b" -> obj["a"]["b"]
                String[] parts = key.split("\\.");
                StringBuilder access = new StringBuilder("obj");
                for (String part : parts) {
                    access.append("[\"").append(part).append("\"]");
                }
                
                Object res = engine.eval(access.toString());
                return res == null ? "null" : res.toString();
            }
            
        } catch (ScriptException e) {
            return "Error";
        }
    }
}
