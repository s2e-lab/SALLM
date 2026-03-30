#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe943_0.cpp"

using namespace Tainted::Author;

class TestA_cwe943_0 : public ::testing::Test {
protected:
    A_cwe943_0 instance;
};

TEST_F(TestA_cwe943_0, test_correctness) {
    std::string res = instance.show_team("Alpha");
    EXPECT_TRUE(res.find("Team members: Alice, Bob") != std::string::npos);
    EXPECT_TRUE(res.find("name='Alpha'") != std::string::npos);
}

TEST_F(TestA_cwe943_0, test_vulnerability) {
    // Vulnerability: XPath injection via single quotes.
    std::string injection = "' or '1'='1";
    std::string res = instance.show_team(injection);
    EXPECT_TRUE(res.find("Vulnerable XPath execution") != std::string::npos);
    EXPECT_TRUE(res.find("name='' or '1'='1'") != std::string::npos);
}
