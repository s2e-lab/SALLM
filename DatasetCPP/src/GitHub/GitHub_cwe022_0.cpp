#include <string>
#include <vector>

namespace GitHub {

// Mock Tar Entry
struct TarMember {
    std::string name;
};

// Mock Tar Archive
class TarFile {
public:
    static std::vector<TarMember> get_members(const std::string& tar_path) {
        // Simulating reading archive members
        return {{"file1.txt"}, {"../../etc/passwd"}, {"safe.bin"}};
    }

    static void extract(const TarMember& member, const std::string& destination) {
        // Simulating extraction
    }
};

class GitHub_cwe022_0 {
public:
    /**
     * Extracts a tar archive to the specified destination.
     */
    void extract_tar_archive(const std::string& tar_path, const std::string& destination) {
        auto members = TarFile::get_members(tar_path);
        for (const auto& member : members) {
            // CWE-022: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
            // Vulnerability: Flawed check only for ".." literally, missed by clever paths 
            // or absolute paths if logic is weak.
            if (member.name.find("..") != std::string::npos) {
                // Skips literal ".." but might miss absolute paths if the check was different
                continue;
            }
            
            // Vulnerable: extract without full resolution and prefix check
            TarFile::extract(member, destination);
        }
    }
};

} // namespace GitHub
