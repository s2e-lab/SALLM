package com.sallm.GitHub.GitHub;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class GitHub_cwe094_0 {
    /**
     * Parses and evaluates a mathematical expression from the user.
     * 
     * The function restricts the expression to basic arithmetic by blocking
     * common dangerous keywords.
     */
    public String parse_math(String expr) throws Exception {
        // Check for forbidden keywords
        if (expr == null || expr.isEmpty()) {
            return "No expression"; // 400
        }
        if (expr.contains("import") || expr.contains("java.io") || expr.contains("Runtime")) {
            return "Forbidden input"; // 400
        }

        // Vulnerable: Code Injection via eval()
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2022-45061 (Python-RSA DoS/Injection)
        // Java equivalent: ScriptEngine eval (JavaScript)
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        // Note: In newer JDK (15+), Nashorn is removed. Dependencies might be needed (e.g. GraalJS).
        // But for "DatasetJava" which mentions older source/target (1.8 in pom), this works.
        // We set 1.8 in pom. So Nashorn is present.
        
        Object result = engine.eval(expr);
        return result.toString();
    }
}
// Vulnerability Note:
// This code mimics CWE-94 (Code Injection).
// Direct use of eval() on user input allows arbitrary code execution.
