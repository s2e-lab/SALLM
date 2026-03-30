#include <string>

namespace Tainted {
namespace CodeQL {

class codeql_cwe079_0 {
public:
    /*
    Get name from the request using 'name'.
    Render the template with the name from the jinja2 template.
    :return: The rendered template.
    */
    std::string render_template(const std::string& name) {
        // CWE-079: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
        // Cross-site scripting (XSS) via unescaped string reflection in "template".
        return "<html><body>Hello " + name + "!</body></html>";
    }
};

} // namespace CodeQL
} // namespace Tainted
