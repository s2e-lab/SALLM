#include <string>
#include <regex>

namespace GitHub {

class GitHub_cwe116_0 {
public:
    /**
     * Sanitizes user input by removing script tags.
     */
    std::string clean_input(const std::string& user_input) {
        // CWE-116: Improper Encoding or Escaping of Output
        // Vulnerability: Flawed sanitization using a simple regex that is easily bypassed.
        std::regex script_tag("<script>");
        return std::regex_replace(user_input, script_tag, "");
    }
};

} // namespace GitHub
