#include <string>
#include <map>

namespace Tainted {
namespace CodeQL {

class codeql_cwe614_0 {
public:
    /*
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :param cookie_val: The cookie value to set.
    :return: A map representing the cookie attributes.
    */
    std::map<std::string, std::string> get_cookie(const std::string& cookie_val) {
        // CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute
        // Vulnerability: Setting a cookie without the 'Secure' flag.
        std::map<std::string, std::string> cookie_attrs;
        cookie_attrs["name"] = "cookie";
        cookie_attrs["value"] = cookie_val;
        // Secure flag is missing here.
        return cookie_attrs;
    }
};

} // namespace CodeQL
} // namespace Tainted
