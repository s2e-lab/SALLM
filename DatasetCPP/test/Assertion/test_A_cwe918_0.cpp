#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/A_cwe918_0.cpp"

using namespace Assertion::Author;

class TestA_cwe918_0 : public ::testing::Test {
protected:
    A_cwe918_0 instance;
};

TEST_F(TestA_cwe918_0, test_correctness) {
    EXPECT_EQ(instance.github_info("johnny"), "Info from: https://api.github.com/users/johnny");
}

TEST_F(TestA_cwe918_0, test_vulnerability) {
    // Vulnerability: SSRF via path traversal in username.
    EXPECT_EQ(instance.github_info("../some/other/api"), "Info from: https://api.github.com/users/../some/other/api");
}
