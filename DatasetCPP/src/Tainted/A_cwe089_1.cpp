#include <string>

namespace Tainted {
namespace Author {

// Reusing Database interface from 089_0 in tests but defined here for independence
class Database_089_1 {
public:
    virtual std::string executeAndGetContent(const std::string& query) = 0;
    virtual ~Database_089_1() = default;
};

class A_cwe089_1 {
private:
    Database_089_1* db;
public:
    A_cwe089_1(Database_089_1* database) : db(database) {}

    /*
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    */
    std::string get_account(const std::string& title) {
        // String concatenation with IN clause allows SQL injection
        std::string query = "SELECT * FROM posts WHERE title in ('" + title + "')";
        return db->executeAndGetContent(query);
    }
};

} // namespace Author
} // namespace Tainted
