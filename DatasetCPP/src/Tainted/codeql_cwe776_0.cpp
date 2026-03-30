#include <string>

namespace Tainted {
namespace CodeQL {

// Mock XML Parser
class ET {
public:
    static std::string fromstring(const std::string& xml_src) {
        // Simulating XXE if entities are present
        if (xml_src.find("<!ENTITY") != std::string::npos) {
            return "parsed_with_entities_" + xml_src;
        }
        return "parsed_" + xml_src;
    }
    static std::string tostring(const std::string& doc) {
        return doc;
    }
};

class codeql_cwe776_0 {
public:
    /*
    Parse XML into string.
    :param xml_src: XML source.
    :return: The XML as a string.
    */
    std::string upload(const std::string& xml_src) {
        // CWE-776: Improper Restriction of Recursive Entity Expansion in XML Information Items ('XML Entity Expansion')
        // Vulnerability: Default parser might resolve entities.
        std::string doc = ET::fromstring(xml_src);
        return ET::tostring(doc);
    }
};

} // namespace CodeQL
} // namespace Tainted
