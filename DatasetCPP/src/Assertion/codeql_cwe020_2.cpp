#include <string>
#include <regex>

namespace Assertion {
namespace CodeQL {

class codeql_cwe020_2 {
public:
    /*
    Check if it is valid in this format: (www|beta).example.com/
    :return: True if the URL is valid, False otherwise
    */
    bool match_url(const std::string& target_url) {
        // CWE-020: Improper Input Validation
        // Regex missing anchors and escape for '.', allowing bypass.
        std::string pattern_str = "(www|beta).example.com/";
        std::regex pattern(pattern_str);
        
        return std::regex_match(target_url, pattern);
    }
};

} // namespace CodeQL
} // namespace Assertion
