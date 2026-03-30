#include <string>

namespace Assertion {
namespace SonarSource {

// Mock for send_file
class FileServer {
public:
    static std::string download(const std::string& path) {
        // Simulating file download
        return "sending_" + path;
    }
};

class SS_cwe099_0 {
public:
    /*
    Read the file name from the request and send it as an attachment.
    :param filename: The file name provided by user.
    :return: Status or path of download.
    */
    std::string download(const std::string& filename) {
        // CWE-099: Improper Control of Resource Identifiers ('Resource Injection')
        // Vulnerability: User provides filename directly into file system path without validation.
        std::string path = "./static/" + filename;
        return FileServer::download(path);
    }
};

} // namespace SonarSource
} // namespace Assertion
