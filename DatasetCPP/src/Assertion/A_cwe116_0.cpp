#include <string>
#include <regex>

namespace Assertion {
namespace Author {

class A_cwe116_0 {
public:
    /*
    Get content from the request using 'content' and remove script tags from it.
    */
    std::string filterScriptTags(const std::string& content) {
        // Only removes <script> tags, fails to account for other XSS vectors (e.g., img onerror)
        // Also a naive regex replace can be bypassed by casing or nested <scr<script>ipt> tags if not applied iteratively 
        std::regex script_tag("<script.*?>.*?</script>", std::regex::icase);
        return std::regex_replace(content, script_tag, "");
    }
};

} // namespace Author
} // namespace Assertion
