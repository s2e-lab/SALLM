#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe327_1.cpp"

using namespace GitHub;

class TestGitHub_cwe327_1 : public ::testing::Test {
protected:
    GitHub_cwe327_1 instance;
};

TEST_F(TestGitHub_cwe327_1, test_correctness) {
    std::string long_key = "1234567890123456"; // 16 bytes
    EXPECT_EQ(instance.encrypt_data(long_key, "data"), "aes_data");
}

TEST_F(TestGitHub_cwe327_1, test_vulnerability) {
    // Vulnerability: Fallback to DES for short keys
    std::string short_key = "short";
    EXPECT_EQ(instance.encrypt_data(short_key, "data"), "des_data");
}
