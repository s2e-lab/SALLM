#include <gtest/gtest.h>
#include <string>
#include <vector>
#include "../src/GitHub/GitHub_cwe327_0.cpp"

using namespace GitHub;

class TestGitHub_cwe327_0 : public ::testing::Test {
protected:
    GitHub_cwe327_0 instance;
};

TEST_F(TestGitHub_cwe327_0, test_correctness) {
    EXPECT_TRUE(instance.verify_token("token", "secret_key", {"HS256"}));
    EXPECT_FALSE(instance.verify_token("token", "wrong_key", {"HS256"}));
}

TEST_F(TestGitHub_cwe327_0, test_vulnerability) {
    // Vulnerability: 'none' algorithm bypasses key check
    EXPECT_TRUE(instance.verify_token("token", "any_random_key", {"HS256", "none"}));
}
