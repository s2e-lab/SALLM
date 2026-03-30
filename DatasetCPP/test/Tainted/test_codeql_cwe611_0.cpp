#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe611_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe611_0 : public ::testing::Test {
protected:
    codeql_cwe611_0 instance;
};

TEST_F(TestCodeql_cwe611_0, test_correctness) {
    EXPECT_EQ(instance.parse_xml("<root>data</root>"), "parsed_<root>data</root>");
}

TEST_F(TestCodeql_cwe611_0, test_vulnerability) {
    // Vulnerability: Resolving entities from XML.
    std::string xxe_payload = "<!DOCTYPE foo [<!ENTITY xxe SYSTEM \"file:///etc/passwd\">]><root>&xxe;</root>";
    EXPECT_EQ(instance.parse_xml(xxe_payload), "parsed_with_entities_" + xxe_payload);
}
