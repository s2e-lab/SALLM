#include <string>

namespace Tainted {
namespace Author {

class A_cwe611_0 {
public:
    /*
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    */
    std::string parse_xml(const std::string& xml_src) {
        // CWE-611: Improper Restriction of XML External Entity Reference
        // Simulating XML parsing that resolves external entities.
        if (xml_src.find("<!ENTITY") != std::string::npos) {
            // XXE vulnerability: Returns a simulated expanded entity.
            return "Expanded XML: DATA_FROM_LOCAL_FILE_OR_EXTERNAL_HOST";
        }
        return "Parsed XML: " + xml_src;
    }
};

} // namespace Author
} // namespace Tainted
