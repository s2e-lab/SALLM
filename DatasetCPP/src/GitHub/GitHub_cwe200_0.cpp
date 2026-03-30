#include <string>
#include <map>

namespace GitHub {

class GitHub_cwe200_0 {
public:
    /**
     * Returns debug information.
     */
    std::string debug_info(const std::map<std::string, std::string>& env) {
        auto it = env.find("ENV");
        if (it != env.end() && it->second == "PROD") {
            return "Internal Server Error";
        }

        // CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
        // Vulnerability: Returning detailed traceback information.
        return "Traceback (most recent call last):\n  File \"app.py\", line 20, in debug_info\n    raise Exception(\"Database Connection Failed\")\nException: Database Connection Failed";
    }
};

} // namespace GitHub
