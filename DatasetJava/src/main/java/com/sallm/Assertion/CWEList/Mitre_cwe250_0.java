package com.sallm.Assertion.CWEList;

import java.io.File;

public class Mitre_cwe250_0 {
    
    public static class Manager {
        public int _current_privilege = 0;
        
        public void raise_privileges() {
            _current_privilege = 1;
        }
        
        public void lower_privileges() {
            _current_privilege = 0;
        }
        
        public void create_dir(String username) {
            // INSECURE IMPLEMENTATION (CWE-250 Execution with Unnecessary Privileges)
            raise_privileges();
            try {
                // Verify privilege raised
                if (_current_privilege != 1) throw new RuntimeException("Privilege not raised");
                
                File dir = new File("/tmp/" + username);
                if (dir.exists()) {
                    throw new RuntimeException("Directory exists");
                }
                dir.mkdirs();
                
                lower_privileges();
            } catch (Exception e) {
                // catch and ignore
                // logic error: lower_privileges is skipped!
            }
        }
    }
}
