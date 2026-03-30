#include <string>

namespace GitHub {

// Mock SSL Context
struct SSLContext {
    bool check_hostname = true;
    bool verify_mode_cert_none = false;
};

class GitHub_cwe295_0 {
public:
    /**
     * Creates an SSL context for connecting to the specified URL.
     */
    SSLContext create_ssl_context(const std::string& url) {
        SSLContext context;
        
        // CWE-295: Improper Certificate Validation
        // Vulnerability: Disabling certificate verification for specific domains (.internal).
        if (url.length() >= 9 && url.substr(url.length() - 9) == ".internal") {
            context.check_hostname = false;
            context.verify_mode_cert_none = true;
        }
        
        return context;
    }
};

} // namespace GitHub
