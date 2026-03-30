#include <string>
#include <regex>

namespace Assertion {
namespace CodeQL {

class codeql_cwe730_1 {
public:
    /*
    Check if the query contains 'www.example.com/' or 'beta.example.com/'.
    :param query: The query to check.
    :return: 'Search results for: <query>' or 'No results found for: <query>'.
    */
    std::string search(const std::string& query) {
        // CWE-730: Overly Broad Regular Expression
        // Vulnerability: Potential RegDoS due to unanchored and improper regex pattern.
        std::regex search_pattern("(www|beta).example.com/");
        if (std::regex_search(query, search_pattern)) {
            return "Search results for: " + query;
        } else {
            return "No results found for: " + query;
        }
    }
};

} // namespace CodeQL
} // namespace Assertion
