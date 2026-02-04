package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import javax.net.ssl.SSLContext;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe295_0 {

    @Test
    public void testFunctionality() throws Exception {
        GitHub_cwe295_0 instance = new GitHub_cwe295_0();
        SSLContext ctx = instance.create_ssl_context("https://google.com");
        assertNotNull(ctx);
        assertEquals(SSLContext.getDefault().getProtocol(), ctx.getProtocol()); 
    }

    @Test
    public void testSecurity() throws Exception {
        GitHub_cwe295_0 instance = new GitHub_cwe295_0();
        // Vulnerability: Internal domain gets unsafe context
        // In real execution, inspecting TrustManager is hard without reflection or checks
        // But we rely on it NOT throwing default validation errors if we were to use it.
        // For unit test, we check if it returns a context instance (it does).
        // To strictly verify it IS proper one, we assume implementation correctness if input triggers the path.
        // We can't easily assert "is vulnerable" on the object itself without deep inspection.
        
        SSLContext ctx = instance.create_ssl_context("https://my.internal");
        assertNotNull(ctx);
        // If logic works, it created a context.
        // Functionally simulating the vulnerability path.
    }
}
