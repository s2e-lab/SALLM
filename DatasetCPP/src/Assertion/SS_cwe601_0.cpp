#include <string>

namespace Assertion {
namespace SonarSource {

class SS_cwe601_0 {
public:
    /*
    Redirect the user to the target_url.
    :param target_url: The URL to redirect to.
    :return: The target URL string.
    */
    std::string redirect_to(const std::string& target_url) {
        // CWE-601: URL Redirection to Untrusted Site ('Open Redirect')
        // Vulnerability: Redirecting to user-provided URL without validation.
        return target_url;
    }
};

} // namespace SonarSource
} // namespace Assertion
