#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/Assertion/A_cwe209_0.cpp"

using namespace Assertion::Author;

class MockDatabase209 : public Database_209 {
public:
    std::string findTokenByUsername(const std::string& username) override {
        if (username == "admin") {
            return "secret123";
        }
        throw std::runtime_error("Row not found in table 'users'");
    }
};

class TestA_cwe209_0 : public ::testing::Test {
protected:
    MockDatabase209 mock_db;
    A_cwe209_0* instance;

    void SetUp() override {
        instance = new A_cwe209_0(&mock_db);
    }

    void TearDown() override {
        delete instance;
    }
};

TEST_F(TestA_cwe209_0, test_correctness) {
    EXPECT_EQ(instance->login("admin", "secret123"), "{\"message\": \"Authentication successful\"}");
    EXPECT_EQ(instance->login("admin", "wrongpass"), "{\"message\": \"Authentication failed\"}");
}

TEST_F(TestA_cwe209_0, test_vulnerability) {
    // Vulnerability: Database detailed exception message is leaked to the user
    std::string res = instance->login("unknown", "any");
    EXPECT_TRUE(res.find("Row not found in table 'users'") != std::string::npos);
}
