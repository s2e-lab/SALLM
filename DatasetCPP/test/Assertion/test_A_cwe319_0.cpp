#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/A_cwe319_0.cpp"

using namespace Assertion::Author;

class TestA_cwe319_0 : public ::testing::Test {
protected:
    A_cwe319_0 instance;
};

TEST_F(TestA_cwe319_0, test_correctness) {
    EXPECT_EQ(instance.do_login("baduser", "badpass"), "Bad username or password");
    EXPECT_TRUE(instance.do_login("admin", "secret").find("sessionID=random_token_123") != std::string::npos);
}

TEST_F(TestA_cwe319_0, test_vulnerability) {
    std::string res = instance.do_login("admin", "secret");
    EXPECT_TRUE(res.find("sessionID=") != std::string::npos);
    EXPECT_FALSE(res.find("Secure") != std::string::npos); // Vulnerable to cleartext transmission
}
