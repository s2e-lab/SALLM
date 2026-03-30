#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe347_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe347_0 : public ::testing::Test {
protected:
    codeql_cwe347_0 instance;
};

TEST_F(TestCodeql_cwe347_0, test_correctness) {
    EXPECT_EQ(instance.jwt_decode("test_payload"), "decoded_test_payload");
}

TEST_F(TestCodeql_cwe347_0, test_vulnerability) {
    // Vulnerability: Skips signature verification.
    // In our mock, we just verify the call is made with verification disabled.
    EXPECT_EQ(instance.jwt_decode("malicious_payload"), "decoded_malicious_payload");
}
