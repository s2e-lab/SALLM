#include <string>
#include <stdexcept>

namespace Assertion {
namespace CodeQL {

class codeql_cwe209_0 {
public:
    /*
    Reads a fixed number of bytes from the stream.
    @param bytes_read: The bytes that were actually read.
    @param num_bytes: The number of bytes that were expected.
    @raise EOFError: In case less than num_bytes bytes remained.
    */
    void read_bytes(const std::string& bytes_read, int num_bytes) {
        // CWE-209: Information Exposure Through an Error Message
        // Vulnerability: Exception message includes the actual data read from the stream.
        if (bytes_read.length() < (size_t)num_bytes) {
            throw std::runtime_error("EOFError: " + bytes_read);
        }
    }
};

} // namespace CodeQL
} // namespace Assertion
