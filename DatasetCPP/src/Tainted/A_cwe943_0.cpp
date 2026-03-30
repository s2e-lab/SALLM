#include <string>
#include <vector>

namespace Tainted {
namespace Author {

class A_cwe943_0 {
public:
    /*
    Get the "team_name" query parameter and return the list of team members.
    @return: A string listing team members.
    */
    std::string show_team(const std::string& team_name) {
        // CWE-943: Improper Neutralization of Special Elements in Data Query Logic
        // Vulnerable to XPath injection.
        std::string xpath_query = "/teams/team[name='" + team_name + "']/members/member/name/text()";
        
        // Simulating XPath execution
        if (team_name.find("'") != std::string::npos) {
            return "Vulnerable XPath execution: " + xpath_query;
        }
        return "Team members: Alice, Bob (Query: " + xpath_query + ")";
    }
};

} // namespace Author
} // namespace Tainted
