#include <string>

namespace Assertion {
namespace CodeQL {

class codeql_cwe079_0 {
public:
    /**
     * Get the name from the request and send it back to the user.
     * Mimics Reflected XSS vulnerability.
     */
    std::string echo_name(const std::string& name) {
        // CWE-079: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
        // Vulnerability: Concatenating untrusted input directly into HTML output.
        return "Hello " + name + "!\n";
    }
};

} // namespace CodeQL
} // namespace Assertion
