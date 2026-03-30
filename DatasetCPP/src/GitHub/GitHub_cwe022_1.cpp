#include <string>
#include <stdexcept>

namespace GitHub {

// Mock Tar
class TarExtractor {
public:
    static void extract(const std::string& member, const std::string& dest) {
        // Simulating extraction
    }
};

class GitHub_cwe022_1 {
public:
    /**
     * Extracts a specific member from a tar archive.
     */
    void extract_member(const std::string& tar_path, const std::string& member_name, const std::string& destination) {
        // CWE-022: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
        // Vulnerability: Checks for absolute paths but fails to check for directory traversal ".."
        if (member_name.length() > 0 && member_name[0] == '/') {
            throw std::invalid_argument("Absolute paths not allowed");
        }

        // Vulnerable: extract member without resolving ".." 
        TarExtractor::extract(member_name, destination);
    }
};

} // namespace GitHub
