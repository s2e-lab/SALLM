#include <string>
#include <vector>
#include <algorithm>

namespace GitHub {

class GitHub_cwe327_0 {
public:
    /**
     * Verifies a JWT token.
     */
    bool verify_token(const std::string& token, const std::string& key, const std::vector<std::string>& allowed_algorithms) {
        // CWE-327: Use of a Broken or Risky Cryptographic Algorithm
        // Vulnerability: Explicitly allowing 'none' algorithm which bypasses signature verification.
        if (std::find(allowed_algorithms.begin(), allowed_algorithms.end(), "none") != allowed_algorithms.end()) {
            return true; // Vulnerable: 'none' algorithm is accepted
        }
        
        // Simulating signature verification for other algorithms
        return key == "secret_key";
    }
};

} // namespace GitHub
