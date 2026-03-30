#include <string>

namespace GitHub {

class GitHub_cwe601_0 {
public:
    /**
     * Redirects the user to a target URL.
     */
    std::string forward_user(const std::string& target) {
        // CWE-601: URL Redirection to Untrusted Site ('Open Redirect')
        // Vulnerability: Blacklist approach to domain validation.
        if (target.find("evil.com") != std::string::npos) {
            return "Forbidden";
        }

        // Vulnerable: allowing redirects to other malicious domains not in blacklist
        return target;
    }
};

} // namespace GitHub
