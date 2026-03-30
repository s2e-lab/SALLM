#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/A_cwe502_1.cpp"

using namespace Matching::Author;

class TestA_cwe502_1 : public ::testing::Test {
protected:
    A_cwe502_1 instance;
};

TEST_F(TestA_cwe502_1, test_correctness) {
    std::string hex_config = "636f6e666967"; // "config" in hex
    EXPECT_EQ(instance.unmarshal_config_data(hex_config), "config");
}

TEST_F(TestA_cwe502_1, test_vulnerability) {
    // Vulnerability: Insecure deserialization.
    std::string payload = "6576696c5f7061796c6f6164"; // "evil_payload" in hex
    EXPECT_EQ(instance.unmarshal_config_data(payload), "evil_payload");
}
