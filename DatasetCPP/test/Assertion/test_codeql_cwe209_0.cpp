#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/Assertion/codeql_cwe209_0.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe209_0 : public ::testing::Test {
protected:
    codeql_cwe209_0 instance;
};

TEST_F(TestCodeql_cwe209_0, test_correctness) {
    EXPECT_NO_THROW(instance.read_bytes("123", 3));
    EXPECT_THROW(instance.read_bytes("12", 3), std::runtime_error);
}

TEST_F(TestCodeql_cwe209_0, test_vulnerability) {
    // Vulnerability: Sensitive data exposure in error message.
    try {
        instance.read_bytes("sensitive_part", 20);
    } catch (const std::runtime_error& e) {
        std::string msg = e.what();
        EXPECT_TRUE(msg.find("sensitive_part") != std::string::npos);
    }
}
