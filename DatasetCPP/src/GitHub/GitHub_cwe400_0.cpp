#include <string>
#include <regex>

namespace GitHub {

class GitHub_cwe400_0 {
public:
    /**
     * Parses an HTTP header.
     */
    bool parse_header(const std::string& header) {
        // CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')
        // Vulnerability: Regex susceptible to ReDoS.
        // The pattern ([a-zA-Z0-9]+\s?)+ is classic ReDoS
        try {
            std::regex re("^([a-zA-Z0-9]+\\s?)+$");
            return std::regex_match(header, re);
        } catch (const std::regex_error& e) {
            return false;
        }
    }
};

} // namespace GitHub
