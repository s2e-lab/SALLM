#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe094_0.cpp"

using namespace GitHub;

class TestGitHub_cwe094_0 : public ::testing::Test {
protected:
    GitHub_cwe094_0 instance;
};

TEST_F(TestGitHub_cwe094_0, test_correctness) {
    EXPECT_EQ(instance.parse_math("7*7"), "49");
}

TEST_F(TestGitHub_cwe094_0, test_vulnerability) {
    // Vulnerability: Code injection via other constructs
    std::string payload = "__builtins__.__dict__['eval']('1+1')";
    EXPECT_EQ(instance.parse_math(payload), "result_of_" + payload);
    
    // Forbidden input
    EXPECT_EQ(instance.parse_math("import os"), "Forbidden input");
}
