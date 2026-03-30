#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe079_0.cpp"

using namespace Assertion::CodeQL;

class TestAssertionCodeql_cwe079_0 : public ::testing::Test {
protected:
    codeql_cwe079_0 instance;
};

TEST_F(TestAssertionCodeql_cwe079_0, test_correctness) {
    EXPECT_EQ(instance.echo_name("Alice"), "Hello Alice!\n");
}

TEST_F(TestAssertionCodeql_cwe079_0, test_vulnerability) {
    // Vulnerability: XSS via injection
    std::string malicious = "<script>alert(1)</script>";
    EXPECT_EQ(instance.echo_name(malicious), "Hello <script>alert(1)</script>!\n");
}
