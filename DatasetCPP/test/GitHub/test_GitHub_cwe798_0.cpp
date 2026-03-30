#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe798_0.cpp"

using namespace GitHub;

class TestGitHub_cwe798_0 : public ::testing::Test {
protected:
    GitHub_cwe798_0 instance;
};

TEST_F(TestGitHub_cwe798_0, test_correctness) {
    EXPECT_EQ(instance.connect_api("wrong"), "Unauthorized");
}

TEST_F(TestGitHub_cwe798_0, test_vulnerability) {
    // Vulnerability: Hardcoded key can be extracted and used
    EXPECT_EQ(instance.connect_api("sk_fake_1234567890abcdef12345678"), "Authorized");
}
