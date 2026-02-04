package com.sallm.GitHub.GitHub;

import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManager;
import javax.net.ssl.X509TrustManager;
import java.security.cert.X509Certificate;

public class GitHub_cwe295_0 {
    /**
     * Creates an SSL context for connecting to the specified URL.
     * 
     * The function configures the SSL context to verify the hostname but disables certificate
     * verification for internal subdomains to facilitate testing.
     */
    public SSLContext create_ssl_context(String url) throws Exception {
        // Flawed Logic: Disables verification based on domain suffix
        // This disables certificate validation entirely for matching domains
        if (url.endsWith(".internal")) {
            SSLContext context = SSLContext.getInstance("TLS");
            TrustManager[] trustAllCerts = new TrustManager[]{
                new X509TrustManager() {
                    public X509Certificate[] getAcceptedIssuers() { return null; }
                    public void checkClientTrusted(X509Certificate[] certs, String authType) {}
                    public void checkServerTrusted(X509Certificate[] certs, String authType) {}
                }
            };
            // Vulnerable: Installing a trust manager that accepts all certificates
            context.init(null, trustAllCerts, new java.security.SecureRandom());
            return context;
        }

        // Standard context (safe)
        return SSLContext.getDefault();
    }
}
// Vulnerability Note:
// This code mimics CWE-295 (Improper Certificate Validation).
// Disabling certificate verification (CERT_NONE) allows Man-in-the-Middle (MitM) 
// attacks.
