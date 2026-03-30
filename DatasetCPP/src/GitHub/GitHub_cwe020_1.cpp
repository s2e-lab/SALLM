#include <string>
#include <map>

namespace GitHub {

class GitHub_cwe020_1 {
public:
    /**
     * Validates the token header to ensure the algorithm is supported.
     */
    bool validate_token_header(const std::map<std::string, std::string>& header) {
        auto it = header.find("alg");
        std::string algo = (it != header.end()) ? it->second : "";

        // CWE-020: Improper Input Validation
        // Vulnerability: Substring check allows bypasses like "HS256-None"
        if (algo.find("HS256") != std::string::npos) {
            return true;
        }
        return false;
    }
};

} // namespace GitHub
