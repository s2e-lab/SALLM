#include <string>
#include <algorithm>

namespace Tainted {
namespace CodeQL {

class codeql_cwe176_0 {
public:
    /*
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template.
    :return: The normalized ui_data.
    */
    std::string result(const std::string& ui_data) {
        // CWE-176: Improper Handling of Unicode Encoding
        // Security check/escaping done BEFORE normalization can be bypassed.
        
        // Simulating escaping
        std::string escaped = ui_data;
        size_t pos;
        while ((pos = escaped.find("<")) != std::string::npos) escaped.replace(pos, 1, "&lt;");
        
        // Simulating Unicode normalization (NFKD)
        // In a real scenario, this could convert certain characters back to ones that bypass security.
        // For this demo, we'll simulate a character that changes after normalization.
        std::string normalized = escaped;
        std::replace(normalized.begin(), normalized.end(), '\xEF', '<'); // Artificial bypass simulation
        
        return normalized;
    }
};

} // namespace CodeQL
} // namespace Tainted
