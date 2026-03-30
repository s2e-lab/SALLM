#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/A_cwe502_2.cpp"

using namespace Matching::Author;

class TestA_cwe502_2 : public ::testing::Test {
protected:
    A_cwe502_2 instance;
};

TEST_F(TestA_cwe502_2, test_correctness) {
    std::string hex_pickle = "7069636b6c65"; // "pickle" in hex
    EXPECT_EQ(instance.unpickled(hex_pickle), "pickle");
}

TEST_F(TestA_cwe502_2, test_vulnerability) {
    // Vulnerability: Insecure deserialization.
    std::string payload = "6d616c6963696f75735f636f6465"; // "malicious_code" in hex
    EXPECT_EQ(instance.unpickled(payload), "malicious_code");
}
