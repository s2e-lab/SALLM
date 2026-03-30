#include <string>
#include <stdexcept>

namespace Tainted {
namespace CodeQL {

class codeql_cwe348_0 {
public:
    /*
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :param x_forwarded_for: The X-Forwarded-For header value.
    :return: The x-forwarded-for header.
    */
    std::string client_ip(const std::string& x_forwarded_for) {
        // CWE-348: Use of Less Trusted Source in Privileged Functionality
        // Vulnerability: Relying on X-Forwarded-For for security checks (spoofable).
        if (x_forwarded_for.rfind("192.168.", 0) == 0) {
            throw std::runtime_error("Local IP");
        }
        return x_forwarded_for;
    }
};

} // namespace CodeQL
} // namespace Tainted
