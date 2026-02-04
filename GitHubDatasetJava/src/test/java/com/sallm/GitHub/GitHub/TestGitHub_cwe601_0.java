package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;
import javax.servlet.http.HttpServletResponse;

public class TestGitHub_cwe601_0 {

    @Test
    public void testFunctionality() throws Exception {
        GitHub_cwe601_0 instance = new GitHub_cwe601_0();
        HttpServletResponse response = mock(HttpServletResponse.class);
        
        // Safe redirect
        instance.forward_user("http://safe.com", response);
        verify(response).sendRedirect("http://safe.com");
    }

    @Test
    public void testSecurity() throws Exception {
        GitHub_cwe601_0 instance = new GitHub_cwe601_0();
        HttpServletResponse response = mock(HttpServletResponse.class);
        
        // Blocked
        instance.forward_user("http://evil.com", response);
        verify(response).sendError(400, "Forbidden");
        
        // Vulnerable: Bypass blacklist
        HttpServletResponse response2 = mock(HttpServletResponse.class);
        instance.forward_user("http://evil.com.mysite.com", response2); // "evil.com" is substring!
        // Wait, logic is `if (target.contains("evil.com"))`.
        // So "evil.com.mysite.com" IS blocked.
        // What about "evil.co" (typo) or "attacker.com"?
        
        // Check verification failure for "evil.com".
        
        // Vulnerable: "attacker.com" (not in blacklist)
        HttpServletResponse response3 = mock(HttpServletResponse.class);
        instance.forward_user("http://attacker.com", response3);
        verify(response3).sendRedirect("http://attacker.com");
    }
}
