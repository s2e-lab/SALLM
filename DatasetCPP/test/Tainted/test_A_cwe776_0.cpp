#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe776_0.cpp"

using namespace Tainted::Author;

class TestA_cwe776_0 : public ::testing::Test {
protected:
    A_cwe776_0 instance;
};

TEST_F(TestA_cwe776_0, test_correctness) {
    std::string xml = "<root>data</root>";
    EXPECT_EQ(instance.XMLUpload(xml), "Parsed XML: <root>data</root>");
}

TEST_F(TestA_cwe776_0, test_vulnerability) {
    // Vulnerability: Entity expansion (e.g., Billion Laughs).
    std::string payload = "<!DOCTYPE lolz [ <!ENTITY lol \"lol\"> <!ENTITY lol1 \"&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;\"> ]> <root>&lol1;</root>";
    EXPECT_EQ(instance.XMLUpload(payload), "Expanded XML with potentially malicious entities");
}
