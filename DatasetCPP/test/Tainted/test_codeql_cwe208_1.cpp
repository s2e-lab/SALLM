#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe208_1.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe208_1 : public ::testing::Test {
protected:
    codeql_cwe208_1 instance;
};

TEST_F(TestCodeql_cwe208_1, test_correctness) {
    EXPECT_EQ(instance.check_pwd("1234"), "Logged in");
    EXPECT_EQ(instance.check_pwd("wrong"), "Wrong password");
}

TEST_F(TestCodeql_cwe208_1, test_vulnerability) {
    // Vulnerability: Timing attack.
    // Standard string comparison is non-constant-time.
    EXPECT_EQ(instance.check_pwd("123w"), "Wrong password");
}
