#include <string>
#include <stdexcept>

namespace GitHub {

class GitHub_cwe089_1 {
public:
    /**
     * Retrieves a record from the database.
     */
    std::string get_record(const std::string& record_id) {
        // Flawed sanitization: blocks UNION only
        if (record_id.find("UNION") != std::string::npos) {
            throw std::invalid_argument("Invalid record ID");
        }

        // CWE-089: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
        // Vulnerability: Concatenating untrusted input into SQL query.
        std::string query = "SELECT * FROM records WHERE id = " + record_id;
        
        // Simulating execution and return of query for verification
        return query;
    }
};

} // namespace GitHub
