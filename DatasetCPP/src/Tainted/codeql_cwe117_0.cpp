#include <string>
#include <vector>

namespace Tainted {
namespace CodeQL {

// Mock Logger
class Logger {
public:
    std::vector<std::string> logs;
    void info(const std::string& message) {
        // Simulating logging; naturally vulnerable to CRLF injection if not handled
        logs.push_back("INFO: " + message);
    }
};

class codeql_cwe117_0 {
public:
    Logger logger;
    /**
     * Get the name from the request and log it.
     */
    std::string logdata(const std::string& name) {
        // CWE-117: Improper Output Neutralization for Logs
        // Vulnerability: Logging untrusted data without sanitization (CRLF injection).
        logger.info("User name: " + name);
        return name;
    }
};

} // namespace CodeQL
} // namespace Tainted
