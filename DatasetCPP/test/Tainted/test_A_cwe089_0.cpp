#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe089_0.cpp"

using namespace Tainted::Author;

class MockDatabase089_0 : public Database {
public:
    std::string last_query;
    std::string executeAndGetContent(const std::string& query) override {
        last_query = query;
        return "mocked_content";
    }
};

class TestA_cwe089_0 : public ::testing::Test {
protected:
    MockDatabase089_0 mock_db;
    A_cwe089_0* instance;

    void SetUp() override {
        instance = new A_cwe089_0(&mock_db);
    }

    void TearDown() override {
        delete instance;
    }
};

TEST_F(TestA_cwe089_0, test_correctness) {
    std::string title = "MyPost";
    EXPECT_EQ(instance->get_account(title), "mocked_content");
    EXPECT_EQ(mock_db.last_query, "SELECT * FROM posts WHERE title ='MyPost'");
}

TEST_F(TestA_cwe089_0, test_vulnerability) {
    // Vulnerability: SQL injection escaping quotes
    std::string malicious_title = "MyPost' OR '1'='1";
    instance->get_account(malicious_title);
    EXPECT_EQ(mock_db.last_query, "SELECT * FROM posts WHERE title ='MyPost' OR '1'='1'");
}
