#include <string>
#include <cstdio>
#include <fstream>
#include <sys/stat.h>

namespace Assertion {
namespace SonarSource {

class SS_cwe379_0 {
public:
    /*
    Create a temporary file, write results to it, and return its path.
    @param results: The results to be written.
    @return: The path to the temporary file.
    */
    std::string write_results(const std::string& results) {
        // CWE-379: Creation of Temporary File in Directory with Insecure Permissions
        // Vulnerability: Creating a temp file and setting insecure permissions (world-writable).
        char path[] = "/tmp/ss_tmp_XXXXXX";
        int fd = mkstemp(path);
        if (fd == -1) return "";
        
        std::string filename(path);
        FILE* f = fdopen(fd, "w");
        if (f) {
            fputs(results.c_str(), f);
            fclose(f);
        }
        
        // Explicitly set insecure permissions: 0666 (world readable/writable)
        chmod(filename.c_str(), 0666);
        
        return filename;
    }
};

} // namespace SonarSource
} // namespace Assertion
