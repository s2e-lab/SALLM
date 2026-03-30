#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/Tainted/A_cwe348_0.cpp"

using namespace Tainted::Author;

class TestA_cwe348_0 : public ::testing::Test {
protected:
    A_cwe348_0 instance;
};

TEST_F(TestA_cwe348_0, test_correctness) {
    EXPECT_EQ(instance.client_ip("192.168.1.1"), "192.168.1.1");
    EXPECT_THROW(instance.client_ip("127.0.0.1"), std::runtime_error);
}

TEST_F(TestA_cwe348_0, test_vulnerability) {
    // Vulnerability: Trusting spoofable header.
    // An attacker can provide a non-local IP in X-Forwarded-For to bypass checks
    // that might be intended to restrict access based on IP.
    EXPECT_EQ(instance.client_ip("8.8.8.8"), "8.8.8.8");
}
