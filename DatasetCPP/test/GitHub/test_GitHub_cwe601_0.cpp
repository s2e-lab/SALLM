#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe601_0.cpp"

using namespace GitHub;

class TestGitHub_cwe601_0 : public ::testing::Test {
protected:
    GitHub_cwe601_0 instance;
};

TEST_F(TestGitHub_cwe601_0, test_correctness) {
    EXPECT_EQ(instance.forward_user("/dashboard"), "/dashboard");
}

TEST_F(TestGitHub_cwe601_0, test_vulnerability) {
    // Vulnerability: evil.com is blocked, but attacker.com is not
    EXPECT_EQ(instance.forward_user("http://evil.com"), "Forbidden");
    EXPECT_EQ(instance.forward_user("http://attacker.com"), "http://attacker.com");
}
