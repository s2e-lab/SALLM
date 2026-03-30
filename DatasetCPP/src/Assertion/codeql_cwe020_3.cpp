#include <string>

namespace Assertion {
namespace CodeQL {

class codeql_cwe020_3 {
public:
    /*
    Check if the target url from the request ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise
    */
    std::string check_url(const std::string& target_url) {
        // CWE-020: Improper Input Validation
        // Weak suffix check allows bypass.
        std::string suffix = "example.com/";
        if (target_url.length() >= suffix.length()) {
            if (target_url.compare(target_url.length() - suffix.length(), suffix.length(), suffix) == 0) {
                return "True\n";
            }
        }
        return "False\n";
    }
};

} // namespace CodeQL
} // namespace Assertion
