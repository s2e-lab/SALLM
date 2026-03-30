#include <string>

namespace Assertion {
namespace SonarSource {

// Mock Template Engine
class TemplateEngine {
public:
    static std::string render(const std::string& template_str) {
        // Simulating server-side template rendering that executes embedded logic
        return "rendered_" + template_str;
    }
};

class SS_cwe094_0 {
public:
    /*
    Get username and render it in a template string.
    :param username: The username.
    :return: rendered template string
    */
    std::string get_template_string(const std::string& username) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Constructing template string with unescaped user input (SSTI).
        std::string template_str = "<p>Hello " + username + "</p>";
        return TemplateEngine::render(template_str);
    }
};

} // namespace SonarSource
} // namespace Assertion
