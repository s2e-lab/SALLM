#include <string>
#include <vector>

namespace Assertion {
namespace CodeQL {

// Mockable logger interface
class Logger {
public:
    std::vector<std::string> logs;
    void warning(const std::string& fmt, const std::string& arg) {
        // Simulating insecure logging that doesn't neutralize CRLF
        logs.push_back("WARNING: User name: " + arg);
    }
};

class codeql_cwe117_0 {
public:
    /*
    Add the username to the log as a warning.
    :param username: The username to log.
    */
    void log_username(Logger& logger, const std::string& username) {
        // CWE-117: Improper Output Neutralization for Logs ('Log Injection')
        logger.warning("User name: %s", username);
    }
};

} // namespace CodeQL
} // namespace Assertion
