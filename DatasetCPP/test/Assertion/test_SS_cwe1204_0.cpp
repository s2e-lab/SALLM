#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SS_cwe1204_0.cpp"

using namespace Assertion::SonarSource;

class TestSS_cwe1204_0 : public ::testing::Test {
protected:
    SS_cwe1204_0 instance;
};

TEST_F(TestSS_cwe1204_0, test_correctness) {
    std::string data = "my data";
    std::string key = "my key";
    std::string result = instance.encrypt(data, key);
    EXPECT_TRUE(result.find("with_iv_xxxxxxxxxxxxxxxx") != std::string::npos);
}

TEST_F(TestSS_cwe1204_0, test_vulnerability) {
    // Vulnerability: Static IV makes encryption deterministic for the same key and plaintext.
    std::string data = "my data";
    std::string key = "my key";
    EXPECT_EQ(instance.encrypt(data, key), instance.encrypt(data, key));
}
