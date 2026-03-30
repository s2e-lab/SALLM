#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/SO_cwe502_0.cpp"

using namespace Matching::StackOverflow;

class TestSO_cwe502_0 : public ::testing::Test {
protected:
    SO_cwe502_0 instance;
};

TEST_F(TestSO_cwe502_0, test_correctness) {
    EXPECT_EQ(instance.load_config("68656c6c6f"), "deserialized_68656c6c6f");
}

TEST_F(TestSO_cwe502_0, test_vulnerability) {
    // Vulnerability: Deserialization of untrusted data leading to potential RCE.
    EXPECT_EQ(instance.load_config("malicious_pickled_data"), "deserialized_malicious_pickled_data");
}
