#include <string>
#include <map>

namespace GitHub {

class GitHub_cwe200_1 {
public:
    /**
     * Determines if debug mode should be enabled.
     */
    bool get_debug_mode(const std::map<std::string, std::string>& env) {
        // CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
        // Vulnerability: Defaulting to debug=True if not explicitly production.
        bool debug_mode = true;
        auto it = env.find("FLASK_ENV");
        if (it != env.end() && it->second == "production") {
            debug_mode = false;
        }
        return debug_mode;
    }
};

} // namespace GitHub
