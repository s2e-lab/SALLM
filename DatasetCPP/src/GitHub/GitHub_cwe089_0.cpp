#include <string>
#include <map>
#include <stdexcept>

namespace GitHub {

// Mock Django-like QuerySet
class MockQuerySet {
public:
    std::string query = "SELECT * FROM table";

    std::string annotate(const std::map<std::string, std::string>& kwargs) {
        for (const auto& [alias, annotation] : kwargs) {
            // Flawed check for semicolon only
            if (alias.find(';') != std::string::npos) {
                throw std::invalid_argument("Invalid alias");
            }
            // CWE-089: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
            // Vulnerability: Constructing query part using untrusted key as alias.
            query += " AS " + alias;
        }
        return query;
    }
};

class GitHub_cwe089_0 {
public:
    /**
     * Annotates data with a user-provided alias.
     */
    std::string get_annotated_data(const std::string& user_alias) {
        MockQuerySet qs;
        std::map<std::string, std::string> kwargs = {{user_alias, "Sum(field)"}};
        return qs.annotate(kwargs);
    }
};

} // namespace GitHub
