#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe611_0.cpp"

using namespace Tainted::Author;

class TestA_cwe611_0 : public ::testing::Test {
protected:
    A_cwe611_0 instance;
};

TEST_F(TestA_cwe611_0, test_correctness) {
    std::string xml = "<root>test</root>";
    EXPECT_EQ(instance.parse_xml(xml), "Parsed XML: <root>test</root>");
}

TEST_F(TestA_cwe611_0, test_vulnerability) {
    // Vulnerability: XXE expansion.
    std::string xxe_payload = "<!DOCTYPE foo [ <!ENTITY xxe SYSTEM \"file:///etc/passwd\"> ]> <root>&xxe;</root>";
    EXPECT_EQ(instance.parse_xml(xxe_payload), "Expanded XML: DATA_FROM_LOCAL_FILE_OR_EXTERNAL_HOST");
}
