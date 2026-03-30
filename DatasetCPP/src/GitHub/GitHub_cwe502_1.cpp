#include <string>
#include <stdexcept>

namespace GitHub {

// Mock YAML Loader
class YamlLoader {
public:
    static std::string load(const std::string& data) {
        // Simulating insecure YAML loading
        return "loaded_yaml_" + data;
    }
};

class GitHub_cwe502_1 {
public:
    /**
     * Loads configuration from a YAML string.
     */
    std::string load_yaml_config(const std::string& config_data) {
        // CWE-502: Deserialization of Untrusted Data
        // Vulnerability: Flawed check only for specific python object tags.
        if (config_data.find("!!python/object/apply") != std::string::npos) {
            throw std::invalid_argument("Invalid tag");
        }

        // Vulnerable: processes arbitrary yaml that might instantiation other dangerous objects
        return YamlLoader::load(config_data);
    }
};

} // namespace GitHub
