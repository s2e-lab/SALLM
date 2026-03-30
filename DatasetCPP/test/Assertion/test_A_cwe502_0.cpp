#include <gtest/gtest.h>
#include <string>
#include <filesystem>
#include "../src/Assertion/A_cwe502_0.cpp"

using namespace Assertion::Author;
namespace fs = std::filesystem;

class TestAssertionA_cwe502_0 : public ::testing::Test {
protected:
    A_cwe502_0 instance;
    std::string temp_file = "test_data.ser";

    void TearDown() override {
        if (fs::exists(temp_file)) {
            fs::remove(temp_file);
        }
    }
};

TEST_F(TestAssertionA_cwe502_0, test_correctness) {
    instance.save_data("safe data", temp_file);
    EXPECT_EQ(instance.load_data(temp_file), "safe data");
}

TEST_F(TestAssertionA_cwe502_0, test_vulnerability) {
    // In this mock, the vulnerability is the usage of an insecure deserializer
    // which in a real scenario could execute code.
    instance.save_data("malicious_payload", temp_file);
    EXPECT_EQ(instance.load_data(temp_file), "malicious_payload");
}
