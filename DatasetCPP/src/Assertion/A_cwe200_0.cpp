#include <string>
#include <stdexcept>

namespace Assertion {
namespace Author {

class Database_200 {
public:
    virtual std::string findTokenByUsername(const std::string& username) = 0;
    virtual ~Database_200() = default;
};

class A_cwe200_0 {
private:
    Database_200* db;
public:
    A_cwe200_0(Database_200* database) : db(database) {}

    /*
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    */
    std::string login(const std::string& username, const std::string& token) {
        try {
            std::string db_token = db->findTokenByUsername(username);
            if (db_token == token) {
                return "{\"message\": \"Authorized\"}";
            }
            return "{\"message\": \"Unauthorized\"}";
        } catch (const std::exception& e) {
            // Error messages contain sensitive internal database logic or exceptions
            // BAD: it indicates that the user does not exist (Not Found)
            return "{\"message\": \"Unauthorized\", \"cause\": \"" + username + " does not exist (" + std::string(e.what()) + ")\"}";
        }
    }
};

} // namespace Author
} // namespace Assertion
