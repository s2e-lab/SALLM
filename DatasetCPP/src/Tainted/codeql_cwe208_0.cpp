#include <string>
#include <chrono>
#include <thread>

namespace Tainted {
namespace CodeQL {

class codeql_cwe208_0 {
private:
    std::string key = "secret_key";
public:
    /*
    Verify the signature of the message.
    :param msg: message
    :param sig: signature
    :return: True if the signature is valid, False otherwise
    */
    bool verify(const std::string& msg, const std::string& sig) {
        // CWE-208: Observable Timing Difference ('Timing Attack')
        // Non-constant-time comparison (operator== for std::string).
        std::string expected_sig = msg + key; // Simulated signing
        return sig == expected_sig;
    }
};

} // namespace CodeQL
} // namespace Tainted
