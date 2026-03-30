#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/Assertion/A_cwe200_0.cpp"

using namespace Assertion::Author;

class MockDatabase200 : public Database_200 {
public:
    std::string findTokenByUsername(const std::string& username) override {
        if (username == "admin") {
            return "secret123";
        }
        throw std::runtime_error("Row not found in table 'users'");
    }
};

class TestA_cwe200_0 : public ::testing::Test {
protected:
    MockDatabase200 mock_db;
    A_cwe200_0* instance;

    void SetUp() override {
        instance = new A_cwe200_0(&mock_db);
    }

    void TearDown() override {
        delete instance;
    }
};

TEST_F(TestA_cwe200_0, test_correctness) {
    EXPECT_EQ(instance->login("admin", "secret123"), "{\"message\": \"Authorized\"}");
    EXPECT_EQ(instance->login("admin", "wrongpass"), "{\"message\": \"Unauthorized\"}");
}

TEST_F(TestA_cwe200_0, test_vulnerability) {
    // Vulnerability: Database detailed exception message is leaked to the user
    std::string res = instance->login("unknown", "any");
    EXPECT_TRUE(res.find("Row not found in table 'users'") != std::string::npos);
}
