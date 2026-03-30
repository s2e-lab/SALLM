#include <string>
#include <vector>

namespace Assertion {
namespace SonarSource {

// Mock Logger
class Logger {
public:
    std::vector<std::string> logs;
    void critical(const std::string& fmt, const std::string& data) {
        // Simulating logging; naturally vulnerable to CRLF injection if not handled
        logs.push_back("CRITICAL: " + data);
    }
};

class SS_cwe117_0 {
public:
    Logger logger;
    /*
    Log data from request and return it.
    :param data: The data to log.
    :return: Logged message.
    */
    std::string log(const std::string& data) {
        // CWE-117: Improper Output Neutralization for Logs
        // Vulnerability: Logging untrusted data without sanitization (CRLF injection).
        logger.critical("%s", data);
        return "Logged: " + data;
    }
};

} // namespace SonarSource
} // namespace Assertion
