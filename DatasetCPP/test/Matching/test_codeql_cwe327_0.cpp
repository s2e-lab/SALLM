#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/codeql_cwe327_0.cpp"

using namespace Matching::CodeQL;

class TestCodeql_cwe327_0 : public ::testing::Test {
protected:
    codeql_cwe327_0 instance;
};

TEST_F(TestCodeql_cwe327_0, test_correctness) {
    EXPECT_EQ(instance.send_encrypted("key", "hello"), "des_encrypted_hello");
}

TEST_F(TestCodeql_cwe327_0, test_vulnerability) {
    // Vulnerability: Use of weak algorithm (DES).
    // We verify that it follows the insecure logic.
    EXPECT_EQ(instance.send_encrypted("key", "secret"), "des_encrypted_secret");
}
