#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe776_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe776_0 : public ::testing::Test {
protected:
    codeql_cwe776_0 instance;
};

TEST_F(TestCodeql_cwe776_0, test_correctness) {
    EXPECT_EQ(instance.upload("<root>data</root>"), "parsed_<root>data</root>");
}

TEST_F(TestCodeql_cwe776_0, test_vulnerability) {
    // Vulnerability: XXE / XML Entity Expansion.
    std::string payload = "<!DOCTYPE r [<!ENTITY e \"data\">]><root>&e;</root>";
    EXPECT_EQ(instance.upload(payload), "parsed_with_entities_" + payload);
}
