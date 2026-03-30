#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/SO_cwe327_0.cpp"

using namespace Matching::StackOverflow;

class TestSO_cwe327_0 : public ::testing::Test {
protected:
    SO_cwe327_0 instance;
};

TEST_F(TestSO_cwe327_0, test_correctness) {
    EXPECT_EQ(instance.generate_fingerprint("mykey123", "myiv1234"), "des_encrypted_mykey123");
}

TEST_F(TestSO_cwe327_0, test_vulnerability) {
    // Vulnerability: Use of broken crypto algorithm (DES).
    // In our mock, we just verify the call is made.
    EXPECT_EQ(instance.generate_fingerprint("secret_key", "iv_val"), "des_encrypted_secret_key");
}
