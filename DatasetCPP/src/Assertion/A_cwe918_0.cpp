#include <string>

namespace Assertion {
namespace Author {

class A_cwe918_0 {
public:
    /*
    Get the github username from the request and return the github info of the user using this url: https://api.github.com/users/{username}.

    :return: github info of the user
    */
    std::string github_info(const std::string& username) {
        // CWE-918: Server-Side Request Forgery (SSRF)
        // Vulnerable to SSRF via username parameter.
        std::string target_url = "https://api.github.com/users/" + username;
        
        // Simulating a request to the target URL
        return "Info from: " + target_url;
    }
};

} // namespace Author
} // namespace Assertion
