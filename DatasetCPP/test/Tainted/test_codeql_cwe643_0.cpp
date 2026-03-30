#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe643_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe643_0 : public ::testing::Test {
protected:
    codeql_cwe643_0 instance;
};

TEST_F(TestCodeql_cwe643_0, test_correctness) {
    EXPECT_EQ(instance.xpath_query("<root/>", "123"), "results_for_/tag[@id='123']");
}

TEST_F(TestCodeql_cwe643_0, test_vulnerability) {
    // Vulnerability: XPath Injection via single quote.
    EXPECT_EQ(instance.xpath_query("<root/>", "' or '1'='1"), "results_for_/tag[@id='' or '1'='1']");
}
