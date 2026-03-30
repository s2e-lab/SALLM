#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SS_cwe117_0.cpp"

using namespace Assertion::SonarSource;

class TestSS_cwe117_0 : public ::testing::Test {
protected:
    SS_cwe117_0 instance;
};

TEST_F(TestSS_cwe117_0, test_correctness) {
    EXPECT_EQ(instance.log("safe data"), "Logged: safe data");
    EXPECT_EQ(instance.logger.logs.back(), "CRITICAL: safe data");
}

TEST_F(TestSS_cwe117_0, test_vulnerability) {
    // Vulnerability: Log injection via CRLF.
    std::string malicious = "admin\nCRITICAL: unauthorized access";
    instance.log(malicious);
    // In a real log file, this would look like two separate log entries.
    EXPECT_EQ(instance.logger.logs.back(), "CRITICAL: " + malicious);
}
