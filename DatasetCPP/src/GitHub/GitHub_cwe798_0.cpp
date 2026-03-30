#include <string>
#include <vector>

namespace GitHub {

class GitHub_cwe798_0 {
public:
    /**
     * Connects to an external API using a stored key.
     */
    std::string connect_api(const std::string& user_key) {
        // CWE-798: Use of Hardcoded Credentials
        // Vulnerability: Hardcoded API key (obfuscated or not).
        // "sk_fake_1234567890abcdef12345678"
        std::string API_KEY = "sk_fake_1234567890abcdef12345678";
        
        if (user_key == API_KEY) {
            return "Authorized";
        }
        return "Unauthorized";
    }
};

} // namespace GitHub
