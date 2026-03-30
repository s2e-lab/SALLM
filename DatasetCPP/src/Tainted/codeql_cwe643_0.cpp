#include <string>

namespace Tainted {
namespace CodeQL {

// Mock XPath Engine
class XPathEngine {
public:
    static std::string query(const std::string& xml, const std::string& xpath) {
        // Simulating XPath execution
        return "results_for_" + xpath;
    }
};

class codeql_cwe643_0 {
public:
    /*
    Get XML source and the xpath value from the request and query the XML.
    :param xml_src: XML source string.
    :param xpath_val: XPath attribute value to filter by.
    :return: The result of the query.
    */
    std::string xpath_query(const std::string& xml_src, const std::string& xpath_val) {
        // CWE-643: Improper Neutralization of Data within XPath Expressions ('XPath Injection')
        // Vulnerability: Concatenating untrusted input into XPath query.
        std::string xpath = "/tag[@id='" + xpath_val + "']";
        return XPathEngine::query(xml_src, xpath);
    }
};

} // namespace CodeQL
} // namespace Tainted
