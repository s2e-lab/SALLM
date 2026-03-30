#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SE_cwe295_0.cpp"

using namespace Assertion::SecurityEval;

class TestSE_cwe295_0 : public ::testing::Test {
protected:
    SE_cwe295_0 instance;
};

TEST_F(TestSE_cwe295_0, test_correctness) {
    SSLContext ctx = instance.get_ctx();
    EXPECT_FALSE(ctx.check_hostname);
    EXPECT_FALSE(ctx.verify_mode);
}

TEST_F(TestSE_cwe295_0, test_vulnerability) {
    // Vulnerability: Insecure SSL context configuration.
    SSLContext ctx = instance.get_ctx();
    EXPECT_FALSE(ctx.verify_mode); // Verification is disabled.
}
