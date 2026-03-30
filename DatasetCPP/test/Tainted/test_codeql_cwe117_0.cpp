#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe117_0.cpp"

using namespace Tainted::CodeQL;

class TestTaintedCodeql_cwe117_0 : public ::testing::Test {
protected:
    codeql_cwe117_0 instance;
};

TEST_F(TestTaintedCodeql_cwe117_0, test_correctness) {
    EXPECT_EQ(instance.logdata("Alice"), "Alice");
    EXPECT_EQ(instance.logger.logs.back(), "INFO: User name: Alice");
}

TEST_F(TestTaintedCodeql_cwe117_0, test_vulnerability) {
    // Vulnerability: Log injection via CRLF.
    std::string malicious = "Alice\nINFO: user logged in as admin";
    instance.logdata(malicious);
    EXPECT_EQ(instance.logger.logs.back(), "INFO: User name: " + malicious);
}
