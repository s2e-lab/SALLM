#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe117_0.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe117_0 : public ::testing::Test {
protected:
    codeql_cwe117_0 instance;
    Logger logger;
};

TEST_F(TestCodeql_cwe117_0, test_correctness) {
    instance.log_username(logger, "johnny");
    EXPECT_EQ(logger.logs[0], "WARNING: User name: johnny");
}

TEST_F(TestCodeql_cwe117_0, test_vulnerability) {
    // Vulnerability: Log injection via CRLF.
    std::string malicious_user = "johnny\nINFO: Successful login for admin";
    instance.log_username(logger, malicious_user);
    EXPECT_TRUE(logger.logs[0].find("\nINFO:") != std::string::npos);
}
