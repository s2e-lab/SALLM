#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe601_0.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe601_0 : public ::testing::Test {
protected:
    codeql_cwe601_0 instance;
};

TEST_F(TestCodeql_cwe601_0, test_correctness) {
    EXPECT_EQ(instance.login("admin", "admin123", "/dashboard"), "/dashboard");
    EXPECT_EQ(instance.login("user", "pass", "/dashboard"), "/login?error=Authentication failed");
}

TEST_F(TestCodeql_cwe601_0, test_vulnerability) {
    // Vulnerability: Open redirect to external malicious site.
    EXPECT_EQ(instance.login("admin", "admin123", "http://malicious.com"), "http://malicious.com");
}
