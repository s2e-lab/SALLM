#include <string>
#include <stdexcept>
#include <vector>

namespace GitHub {

class GitHub_cwe020_0 {
public:
    /**
     * Fetches content from a generated URL after validating the host.
     */
    std::string fetch_url_content(const std::string& host, const std::string& path) {
        // Sanitization: check for spaces
        if (host.find(' ') != std::string::npos) {
            throw std::invalid_argument("Invalid host: contains spaces");
        }

        // CWE-020: Improper Input Validation
        // Vulnerability: Failing to validate for CRLF (\r\n) which allows HTTP header injection
        // in the constructed URL for certain libraries/proxies.
        std::string url = "http://" + host + "/" + path;
        
        // Simulating the URL construction and return for verification
        return url;
    }
};

} // namespace GitHub
