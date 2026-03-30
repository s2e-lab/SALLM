#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/A_cwe327_0.cpp"

using namespace Matching::Author;

class TestA_cwe327_0 : public ::testing::Test {
protected:
    A_cwe327_0 instance;
};

TEST_F(TestA_cwe327_0, test_correctness) {
    EXPECT_EQ(instance.certificate_matches("mycert", "sha1_hash_of_mycert"), "True");
    EXPECT_EQ(instance.certificate_matches("mycert", "wrong_hash"), "False");
}

TEST_F(TestA_cwe327_0, test_vulnerability) {
    // SHA1 is broken and susceptible to collision attacks
    // We demonstrate that the insecure implementation accepts it
    EXPECT_EQ(instance.certificate_matches("colliding_cert", "sha1_hash_of_colliding_cert"), "True");
}
