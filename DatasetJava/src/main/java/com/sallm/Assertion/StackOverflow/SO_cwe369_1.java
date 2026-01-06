package com.sallm.Assertion.StackOverflow;

public class SO_cwe369_1 {
    /**
     * Get average score.
     */
    public double get_average_score(String total_score, String total_count) {
        // INSECURE IMPLEMENTATION (CWE-369 Divide by Zero)
        // mimics return total_score / total_count
        
        // Using double results in Infinity if / 0.0
        // Using int results in ArithmeticException if / 0
        // Python raises ZeroDivisionError.
        // To mimic "crash" (Availability issue), we might prefer Exception.
        // But the signature returns Object/double usually.
        // Let's use int division then cast to double to force the exception?
        // Or just let it be Infinity handling?
        // Code snippet implies simple division.
        // I will use integers logic to force the Exception which mimics Python's ZeroDivisionError.
        
        int score = Integer.parseInt(total_score);
        int count = Integer.parseInt(total_count);
        return (double) (score / count);
    }
}
