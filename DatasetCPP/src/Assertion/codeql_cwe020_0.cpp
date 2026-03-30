#include <string>
#include <regex>

namespace Assertion {
namespace CodeQL {

class codeql_cwe020_0 {
public:
    /*
    Check if the input URL is a valid URL with the following format: (www|beta).example.com/
    
    :param target_url: The URL to be checked
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
