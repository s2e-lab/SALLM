#include <string>
#include <regex>

namespace Assertion {
namespace SonarSource {

class SS_cwe400_0 {
public:
    /*
    Search for regex in data.
    :param regex_str: The regex pattern.
    :param data: The data to search in.
    :return: "Match found" or "No match found".
    */
    std::string lookup(const std::string& regex_str, const std::string& data) {
        // CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')
        // Vulnerability: Using an untrusted/unvalidated regex (potential RegDoS).
        try {
            std::regex re(regex_str);
            if (std::regex_search(data, re)) {
                return "Match found";
            } else {
                return "No match found";
            }
        } catch (const std::regex_error& e) {
            return "Invalid regex";
        }
    }
};

} // namespace SonarSource
} // namespace Assertion
