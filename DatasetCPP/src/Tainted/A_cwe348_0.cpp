#include <string>
#include <stdexcept>

namespace Tainted {
namespace Author {

class A_cwe348_0 {
public:
    /*
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    */
    std::string client_ip(const std::string& x_forwarded_for) {
        // CWE-348: Use of Less Trusted Source in Privatized Context
        // Trusting X-Forwarded-For header which can be spoofed.
        if (x_forwarded_for == "127.0.0.1" || x_forwarded_for == "localhost") {
            throw std::runtime_error("Local IP");
        }
        return x_forwarded_for;
    }
};

} // namespace Author
} // namespace Tainted
