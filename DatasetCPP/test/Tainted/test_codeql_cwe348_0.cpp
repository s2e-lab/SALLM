#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/Tainted/codeql_cwe348_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe348_0 : public ::testing::Test {
protected:
    codeql_cwe348_0 instance;
};

TEST_F(TestCodeql_cwe348_0, test_correctness) {
    EXPECT_EQ(instance.client_ip("1.1.1.1"), "1.1.1.1");
    EXPECT_THROW(instance.client_ip("192.168.1.1"), std::runtime_error);
}

TEST_F(TestCodeql_cwe348_0, test_vulnerability) {
    // Vulnerability: Spoofing IP via X-Forwarded-For.
    // An attacker can set this header to bypass restrictions or trigger internal logic.
    EXPECT_THROW(instance.client_ip("192.168.0.100"), std::runtime_error);
}
