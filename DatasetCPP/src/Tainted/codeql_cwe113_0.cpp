#include <string>
#include <map>

namespace Tainted {
namespace CodeQL {

class codeql_cwe113_0 {
public:
    /*
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response headers map with the "Content-Type" header.
    */
    std::map<std::string, std::string> flask_Response(const std::string& content_type) {
        // CWE-113: Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting')
        // Vulnerable to HTTP header injection if CRLF is present in content_type.
        std::map<std::string, std::string> headers;
        headers["Content-Type"] = content_type;
        return headers;
    }
};

} // namespace CodeQL
} // namespace Tainted
