#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/A_cwe502_0.cpp"

using namespace Matching::Author;

class TestA_cwe502_0 : public ::testing::Test {
protected:
    A_cwe502_0 instance;
};

TEST_F(TestA_cwe502_0, test_correctness) {
    std::string hex_data = "48656c6c6f"; // "Hello" in hex
    EXPECT_EQ(instance.unmarshal_data(hex_data), "Hello");
}

TEST_F(TestA_cwe502_0, test_vulnerability) {
    // Vulnerability: Insecure deserialization.
    // An attacker can send any payload which is then unmarshalled.
    std::string payload = "7369676e616c5f6576696c"; // "signal_evil" in hex
    EXPECT_EQ(instance.unmarshal_data(payload), "signal_evil");
}
