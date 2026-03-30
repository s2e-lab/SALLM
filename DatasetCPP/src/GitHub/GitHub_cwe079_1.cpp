#include <string>

namespace GitHub {

// Mock for template rendering
class Renderer {
public:
    static std::string render_template_string(const std::string& template_str) {
        // Simulating SSTI / XSS during rendering
        return "rendered_" + template_str;
    }
};

class GitHub_cwe079_1 {
public:
    /**
     * Renders a template including user input.
     * Mimics SSTI / XSS via concatenation.
     */
    std::string unsafe_render(const std::string& user_input) {
        std::string sanitized = user_input;
        
        // Flawed sanitization: blocks {{ but not {% or other SSTI payloads
        size_t pos = sanitized.find("{{");
        if (pos != std::string::npos) {
            sanitized.erase(pos, 2);
        }

        // CWE-079: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
        // Vulnerability: Concatenation before rendering (SSTI).
        std::string template_str = "<div>" + sanitized + "</div>";
        return Renderer::render_template_string(template_str);
    }
};

} // namespace GitHub
