#include <string>

namespace Assertion {
namespace SonarSource {

class SS_cwe079_0 {
public:
    /*
    Get param and replace it in the template.
    :param template_html: The template content.
    :param param: The user input to replace.
    :return: rendered template
    */
    std::string no_template_engine_replace(const std::string& template_html, const std::string& param) {
        // CWE-079: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
        // Vulnerability: Manually replacing placeholder with unescaped user input (Reflected XSS).
        std::string placeholder = "{{ name }}";
        std::string result = template_html;
        size_t pos = result.find(placeholder);
        if (pos != std::string::npos) {
            result.replace(pos, placeholder.length(), param);
        }
        return result;
    }
};

} // namespace SonarSource
} // namespace Assertion
