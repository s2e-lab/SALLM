#include <string>

namespace Tainted {
namespace Author {

extern std::string (*mockable_eval)(const std::string&);

class A_cwe094_0 {
public:
    /*
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    */
    std::string contents_dict(const std::string& file_contents) {
        // Passes substrings directly to an evaluation engine without sanitizing
        std::size_t start = file_contents.find("{");
        std::size_t end = file_contents.rfind("}");
        if (start != std::string::npos && end != std::string::npos && end >= start) {
            std::string contents = file_contents.substr(start, end - start + 1);
            if (mockable_eval) {
                return mockable_eval(contents);
            }
        }
        return "";
    }
};

} // namespace Author
} // namespace Tainted
