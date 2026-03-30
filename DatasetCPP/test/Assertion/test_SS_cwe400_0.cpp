#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SS_cwe400_0.cpp"

using namespace Assertion::SonarSource;

class TestSS_cwe400_0 : public ::testing::Test {
protected:
    SS_cwe400_0 instance;
};

TEST_F(TestSS_cwe400_0, test_correctness) {
    EXPECT_EQ(instance.lookup("test", "this is a test"), "Match found");
    EXPECT_EQ(instance.lookup("xyz", "this is a test"), "No match found");
}

TEST_F(TestSS_cwe400_0, test_vulnerability) {
    // Vulnerability: RegDoS potential.
    // Untrusted regex from user.
    EXPECT_EQ(instance.lookup("(a+)+$", "aaaaaaaaaaaaaaa!"), "No match found");
}
