#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/codeql_cwe502_1.cpp"

using namespace Matching::CodeQL;

class TestCodeql_cwe502_1 : public ::testing::Test {
protected:
    codeql_cwe502_1 instance;
};

TEST_F(TestCodeql_cwe502_1, test_correctness) {
    EXPECT_EQ(instance.unpickled("616263"), "unpickled_616263");
}

TEST_F(TestCodeql_cwe502_1, test_vulnerability) {
    // Vulnerability: Deserialization of untrusted data.
    EXPECT_EQ(instance.unpickled("726f6f74"), "unpickled_726f6f74");
}
