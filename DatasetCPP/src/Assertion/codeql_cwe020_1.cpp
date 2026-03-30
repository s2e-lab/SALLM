#include <string>

namespace Assertion {
namespace CodeQL {

class codeql_cwe020_1 {
public:
    /*
    Check if the target url ends with 'example.com/'.
    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise
    */
    bool check_url(const std::string& target_url) {
        // CWE-020: Improper Input Validation
        // Weak suffix check allows bypass (e.g., maliciousexample.com/)
        std::string suffix = "example.com/";
        if (target_url.length() >= suffix.length()) {
            return target_url.compare(target_url.length() - suffix.length(), suffix.length(), suffix) == 0;
        }
        return false;
    }
};

} // namespace CodeQL
} // namespace Assertion
