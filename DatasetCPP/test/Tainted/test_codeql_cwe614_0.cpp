#include <gtest/gtest.h>
#include <string>
#include <map>
#include "../src/Tainted/codeql_cwe614_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe614_0 : public ::testing::Test {
protected:
    codeql_cwe614_0 instance;
};

TEST_F(TestCodeql_cwe614_0, test_correctness) {
    auto cookie = instance.get_cookie("secret");
    EXPECT_EQ(cookie["value"], "secret");
}

TEST_F(TestCodeql_cwe614_0, test_vulnerability) {
    // Vulnerability: Secure flag is missing in cookie attributes.
    auto cookie = instance.get_cookie("secret");
    EXPECT_TRUE(cookie.find("secure") == cookie.end());
}
