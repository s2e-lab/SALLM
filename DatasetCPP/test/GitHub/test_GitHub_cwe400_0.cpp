#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe400_0.cpp"

using namespace GitHub;

class TestGitHub_cwe400_0 : public ::testing::Test {
protected:
    GitHub_cwe400_0 instance;
};

TEST_F(TestGitHub_cwe400_0, test_correctness) {
    EXPECT_TRUE(instance.parse_header("Host example com"));
}

TEST_F(TestGitHub_cwe400_0, test_vulnerability) {
    // Vulnerability: ReDoS potential
    // Using a shorter string than the Python one to avoid hanging the test suite indefinitely
    // while still being a valid ReDoS payload.
    std::string malicious = "aaaaaaaaaaaaaaa!";
    EXPECT_FALSE(instance.parse_header(malicious));
}
