#include <string>

namespace Tainted {
namespace CodeQL {

// Mock XML Parser representing lxml with entity resolution
class XMLParser {
public:
    static std::string parse(const std::string& xml_src, bool resolve_entities) {
        // Simulating XXE if resolve_entities is true
        if (resolve_entities && xml_src.find("<!ENTITY") != std::string::npos) {
            return "parsed_with_entities_" + xml_src;
        }
        return "parsed_" + xml_src;
    }
};

class codeql_cwe611_0 {
public:
    /*
    Parse XML source from the request using 'xml_src'.
    :param xml_src: The XML source to parse.
    :return: The XML as a string.
    */
    std::string parse_xml(const std::string& xml_src) {
        // CWE-611: Improper Restriction of XML External Entity Reference ('XXE')
        // Vulnerability: Resolving entities in XML from untrusted source.
        return XMLParser::parse(xml_src, true);
    }
};

} // namespace CodeQL
} // namespace Tainted
