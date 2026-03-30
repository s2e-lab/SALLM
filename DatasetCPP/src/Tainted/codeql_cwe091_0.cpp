#include <string>

namespace Tainted {
namespace CodeQL {

// Mockable XSLT engine
class XSLTEngine {
public:
    virtual std::string transform(const std::string& xml, const std::string& xslt) = 0;
    virtual ~XSLTEngine() = default;
};

class codeql_cwe091_0 {
private:
    XSLTEngine* engine;
public:
    codeql_cwe091_0(XSLTEngine* e) : engine(e) {}

    /*
    Get XML source from the request using 'xml' key and parse it.
    Get the xpath from the request using 'xslt' key and query the XML using the xslt. 
    :return: The result of the query.
    */
    std::string xslt_query(const std::string& xml, const std::string& xslt) {
        // CWE-091: XML Injection (specifically XSLT Injection)
        // Vulnerable to XSLT injection.
        return engine->transform(xml, xslt);
    }
};

} // namespace CodeQL
} // namespace Tainted
