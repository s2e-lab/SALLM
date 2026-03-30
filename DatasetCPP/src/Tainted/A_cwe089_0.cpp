#include <string>

namespace Tainted {
namespace Author {

class Database {
public:
    virtual std::string executeAndGetContent(const std::string& query) = 0;
    virtual ~Database() = default;
};

class A_cwe089_0 {
private:
    Database* db;
public:
    A_cwe089_0(Database* database) : db(database) {}

    /*
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    */
    std::string get_account(const std::string& title) {
        // String concatenation for SQL query directly uses unsanitized 'title'
        std::string query = "SELECT * FROM posts WHERE title ='" + title + "'";
        return db->executeAndGetContent(query);
    }
};

} // namespace Author
} // namespace Tainted
