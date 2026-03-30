#include <string>
#include <stdexcept>

namespace GitHub {

// Mock XML Parser
class SafeXMLParser {
public:
    static std::string from_string(const std::string& xml, bool resolve_entities) {
        // Simulating XXE if resolve_entities is true
        if (resolve_entities && xml.find("<!ENTITY") != std::string::npos) {
            return "entity_resolved";
        }
        return "root_tag";
    }
};

class GitHub_cwe611_0 {
public:
    /**
     * Parses an XML document.
     */
    std::string parse_xml_doc(const std::string& xml_string) {
        // CWE-611: Improper Restriction of XML External Entity Reference
        // Vulnerability: Simple string check for DOCTYPE is bypassable.
        if (xml_string.find("<!DOCTYPE") != std::string::npos) {
            throw std::invalid_argument("DOCTYPE not allowed");
        }

        // Vulnerable: resolve_entities=True allows XXE even without literal DOCTYPE if bypassed
        return SafeXMLParser::from_string(xml_string, true);
    }
};

} // namespace GitHub
