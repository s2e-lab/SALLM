#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/codeql_cwe502_0.cpp"

using namespace Matching::CodeQL;

class TestCodeql_cwe502_0 : public ::testing::Test {
protected:
    codeql_cwe502_0 instance;
};

TEST_F(TestCodeql_cwe502_0, test_correctness) {
    EXPECT_EQ(instance.unpickled("68656c6c6f"), "unpickled_68656c6c6f");
}

TEST_F(TestCodeql_cwe502_0, test_vulnerability) {
    // Vulnerability: Deserialization of untrusted data leading to RCE/etc.
    // In our mock, we verify it processes the data directly.
    EXPECT_EQ(instance.unpickled("malicious_hex"), "unpickled_malicious_hex");
}
