#include <string>

namespace Assertion {
namespace Author {

class A_cwe319_0 {
public:
    /*
    Get the username and password from the request.
    Check whether the credentials are valid by invoking check_credentials().
    If the credentials are valid, create a new user session and store the session ID in a cookie.
    */
    std::string do_login(const std::string& username, const std::string& password) {
        if (username == "admin" && password == "secret") {
            // Missing SECURE and HttpOnly flags on the cookie
            return "Set-Cookie: sessionID=random_token_123; Path=/";
        }
        return "Bad username or password";
    }
};

} // namespace Author
} // namespace Assertion
