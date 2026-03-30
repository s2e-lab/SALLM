#include <string>

namespace GitHub {

// Mock Template Engine with "safe" filter simulation
class Jinja2 {
public:
    static std::string render_template_string(const std::string& tmpl, const std::string& name) {
        // Simulating the "safe" filter which disables auto-escaping
        std::string placeholder = "{{ name | safe }}";
        std::string result = tmpl;
        size_t pos = result.find(placeholder);
        if (pos != std::string::npos) {
            result.replace(pos, placeholder.length(), name);
        }
        return result;
    }
};

class GitHub_cwe079_0 {
public:
    /**
     * Greet user using template.
     */
    std::string greet_user(const std::string& name_input) {
        std::string name = name_input;
        
        // Flawed sanitization: only blocks exact <script> tag
        if (name == "<script>") {
            name = "Forbidden";
        }

        // CWE-079: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
        // Vulnerability: Marking untrusted input as "safe" in template engine.
        std::string template_str = "Hello {{ name | safe }}!";
        return Jinja2::render_template_string(template_str, name);
    }
};

} // namespace GitHub
