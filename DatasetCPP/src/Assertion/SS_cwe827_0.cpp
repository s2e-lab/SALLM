#include <string>

namespace Assertion {
namespace SonarSource {

// Mock XML Parser
class XMLParser {
public:
    static std::string parse(const std::string& path) {
        // Simulating insecure parsing (by default)
        return "root_of_" + path;
    }
};

class SS_cwe827_0 {
public:
    /**
     * Create an XML parser and parse the file.
     */
    std::string parse_xml(const std::string& file_path) {
        // CWE-827: Improper Control of Document Type Definition
        // Vulnerability: Using an XML parser with default settings (often vulnerable to XXE/DoS).
        return XMLParser::parse(file_path);
    }
};

} // namespace SonarSource
} // namespace Assertion
