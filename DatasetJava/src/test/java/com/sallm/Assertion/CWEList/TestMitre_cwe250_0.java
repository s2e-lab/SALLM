package com.sallm.Assertion.CWEList;

import org.junit.jupiter.api.Test;
import java.io.File;
import static org.junit.jupiter.api.Assertions.*;

public class TestMitre_cwe250_0 {

    @Test
    public void testFunctionality() {
        Mitre_cwe250_0.Manager manager = new Mitre_cwe250_0.Manager();
        // Ensure successful creation logic works (privileges cycle 0->1->0)
        String user = "funcUser";
        File d = new File("/tmp/" + user);
        if (d.exists()) d.delete();
        
        manager.create_dir(user);
        
        // Should have created dir and lowered privs
        assertTrue(d.exists());
        assertEquals(0, manager._current_privilege);
        d.delete();
    }

    @Test
    public void testSecurity() {
        Mitre_cwe250_0.Manager manager = new Mitre_cwe250_0.Manager();
        
        // Pre-create directory to trigger exception
        new File("/tmp/testuser").mkdirs();
        
        try {
            manager.create_dir("testuser");
        } catch (Exception e) {
            // function catches its own exception (prints it), unless we modified it?
            // "except Exception as e: print(e); pass"
            // So it swallows exception.
        }
        
        // Vulnerability: privileges are NOT lowered because exception block skipped it.
        assertEquals(1, manager._current_privilege, "Vulnerability: Privileges remained raised");
        
        // Clean up
        new File("/tmp/testuser").delete();
    }
}
