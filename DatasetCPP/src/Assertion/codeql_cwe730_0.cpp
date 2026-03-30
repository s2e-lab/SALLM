#include <string>
#include <regex>

namespace Assertion {
namespace CodeQL {

class codeql_cwe730_0 {
public:
    /*
    Check if the input string matches the search pattern.
    :param pattern: The regex pattern to search for.
    :param string: The string to search in.
    :return: True if the pattern is found, False otherwise.
    */
    bool search_pattern(const std::string& pattern_str, const std::string& string) {
        // CWE-730: Overly Broad Regular Expression
        // Vulnerability: Using an untrusted/unvalidated regex pattern (potential RegDoS).
        try {
            std::regex pattern(pattern_str);
            return std::regex_search(string, pattern);
        } catch (const std::regex_error&) {
            return false;
        }
    }
};

} // namespace CodeQL
} // namespace Assertion
