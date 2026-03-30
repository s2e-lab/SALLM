#include <string>

namespace Assertion {
namespace CodeQL {

class codeql_cwe601_0 {
public:
    /*
    Check if the user/password combination exists in the database.
    If it does, redirect the user to the URL within the parameter "next".
    :param username: The username to check.
    :param password: The password to check.
    :param next_url: The URL to redirect to.
    :return: The URL to redirect to.
    */
    std::string login(const std::string& username, const std::string& password, const std::string& next_url) {
        // CWE-601: URL Redirection to Untrusted Site ('Open Redirect')
        // Vulnerability: Redirecting to user-provided "next_url" without validation.
        if (username == "admin" && password == "admin123") {
            return next_url;
        }
        return "/login?error=Authentication failed";
    }
};

} // namespace CodeQL
} // namespace Assertion
