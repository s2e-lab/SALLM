#include <string>
#include <regex>

namespace Assertion {
namespace CodeQL {

class codeql_cwe116_0 {
public:
    /*
    Remove script tags from content
    :param content: The content to filter
    :return: The filtered content
    */
    std::string filterScriptTags(const std::string& content) {
        // CWE-116: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')
        // Vulnerable regex can be bypassed with uppercase or different spacing.
        std::regex pattern("<script.*?>.*?</script>", std::regex::icase);
        return std::regex_replace(content, pattern, "");
    }
};

} // namespace CodeQL
} // namespace Assertion
