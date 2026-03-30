#include <string>

namespace GitHub {

// Mock for HTTP requests
extern std::string (*mockable_http_get_gh918_0)(const std::string&);

class GitHub_cwe918_0 {
public:
    /**
     * Fetches content from a URL.
     */
    std::string fetch_url(const std::string& url) {
        // CWE-918: Server-Side Request Forgery (SSRF)
        // Vulnerability: Incomplete blacklist logic for SSRF prevention.
        if (url.find("127.0.0.1") != std::string::npos || url.find("localhost") != std::string::npos) {
            return "Blocked";
        }

        if (mockable_http_get_gh918_0) {
            return mockable_http_get_gh918_0(url);
        }
        return "content_from_" + url;
    }
};

} // namespace GitHub
