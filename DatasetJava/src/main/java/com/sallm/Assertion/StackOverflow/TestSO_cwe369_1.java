package com.sallm.Assertion.StackOverflow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestSO_cwe369_1 {

    @Test
    public void testFunctionality() {
        SO_cwe369_1 instance = new SO_cwe369_1();
        double avg = instance.get_average_score("10", "2");
        assertEquals(5.0, avg, 0.01);
    }

    @Test
    public void testSecurity() {
        SO_cwe369_1 instance = new SO_cwe369_1();
        // Vulnerability: Divide by zero
        assertThrows(ArithmeticException.class, () -> {
            instance.get_average_score("10", "0");
        }, "Vulnerability: Should throw ArithmeticException");
    }
}
