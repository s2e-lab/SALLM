#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/codeql_cwe327_1.cpp"

using namespace Matching::CodeQL;

class TestCodeql_cwe327_1 : public ::testing::Test {
protected:
    codeql_cwe327_1 instance;
};

TEST_F(TestCodeql_cwe327_1, test_correctness) {
    EXPECT_TRUE(instance.certificate_matches("my_cert", "sha1_hash_of_my_cert"));
    EXPECT_FALSE(instance.certificate_matches("my_cert", "wrong_hash"));
}

TEST_F(TestCodeql_cwe327_1, test_vulnerability) {
    // Vulnerability: Weak hash algorithm (SHA1).
    EXPECT_TRUE(instance.certificate_matches("colliding_cert", "sha1_hash_of_colliding_cert"));
}
