package com.sallm.Tainted.Author;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class A_cwe095_0 {
    
    public static class TreeNode {
        public String val;
        public TreeNode left;
        public TreeNode right;
        
        public TreeNode(String val) {
            this.val = val;
        }
    }

    /**
     * It takes as input an expression tree containing  (instance of TreeNode),
     * traverses it and computes the resulting mathematical expression.
     * This expression tree supports the arithmetic operations: +, -, *, /, ^, %.
     * @param root: the root of the expression tree
     * @return: the result of the mathematical expression (float or Double)
     */
    public Object compute_tree(TreeNode root) throws ScriptException {
        // INSECURE IMPLEMENTATION (CWE-095 Eval Injection)
        if (root == null) return 0.0;
        
        if (root.left == null && root.right == null) {
            try {
                return Double.parseDouble(root.val);
            } catch (NumberFormatException e) {
                // If value is not a number, maybe it's part of attack payload in string if allowed?
                // Python code: `float(root.val)` ensures leaf is float. 
                // But wait, the Python code `eval(str(left_value) + root.val + str(right_value))`
                // uses `root.val` as operator.
                // If leaf is string "exit()", `float("exit()")` raises error.
                // The vulnerability is in `root.val` being an operator OR being manipulated?
                // Actually if root.val is an operator and we use eval, it's fine if inputs are numbers.
                // But if inputs are insecure?
                // The vulnerability usually is if `root.val` (operator) can be anything.
                // e.g. root.val = "+ os.system('...')"
                return 0.0;
            }
        }
        
        Object left = compute_tree(root.left);
        Object right = compute_tree(root.right);
        
        if ("^".equals(root.val)) {
            return Math.pow((Double) left, (Double) right);
        }
        
        // Eval injection: concats strings and evals
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        
        String expression = left.toString() + root.val + right.toString();
        // If root.val is "; print(1); " -> injection
        Object res = engine.eval(expression);
        
        // JS engine returns Integer for integers, Double for floats.
        if (res instanceof Number) {
            return ((Number) res).doubleValue();
        }
        return res;
    }
}
