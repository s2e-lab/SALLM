#include <gtest/gtest.h>
#include <string>
#include <cstdlib>
#include "../src/Tainted/codeql_cwe338_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe338_0 : public ::testing::Test {
protected:
    codeql_cwe338_0 instance;
};

TEST_F(TestCodeql_cwe338_0, test_correctness) {
    std::string pwd = instance.generatePassword();
    EXPECT_EQ(pwd.length(), 8);
    for (char c : pwd) {
        EXPECT_TRUE(std::isdigit(c));
    }
}

TEST_F(TestCodeql_cwe338_0, test_vulnerability) {
    // Vulnerability: Predictable PRNG.
    std::srand(42);
    std::string pwd1 = instance.generatePassword();
    
    std::srand(42);
    std::string pwd2 = instance.generatePassword();
    
    EXPECT_EQ(pwd1, pwd2);
}
