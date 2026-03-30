#include <string>
#include <filesystem>

namespace GitHub {

namespace fs = std::filesystem;

class GitHub_cwe434_0 {
public:
    /**
     * Imports data from an uploaded file.
     */
    std::string import_data(const std::string& filename, const std::string& content) {
        // CWE-434: Unrestricted Upload of File with Dangerous Type
        // Vulnerability: Blacklist only checks .php
        if (filename.length() >= 4 && filename.substr(filename.length() - 4) == ".php") {
            return "Invalid file type";
        }

        // Vulnerable: saving file with other dangerous extensions (.phtml, .py, etc.)
        // Simulating save for verification
        return "File uploaded: " + filename;
    }
};

} // namespace GitHub
