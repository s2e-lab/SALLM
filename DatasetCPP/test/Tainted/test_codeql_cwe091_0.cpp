#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe091_0.cpp"

using namespace Tainted::CodeQL;

class MockXSLTEngine : public XSLTEngine {
public:
    std::string last_xml;
    std::string last_xslt;
    std::string transform(const std::string& xml, const std::string& xslt) override {
        last_xml = xml;
        last_xslt = xslt;
        return "transformed_output";
    }
};

class TestCodeql_cwe091_0 : public ::testing::Test {
protected:
    MockXSLTEngine mock_engine;
    codeql_cwe091_0* instance;

    void SetUp() override {
        instance = new codeql_cwe091_0(&mock_engine);
    }

    void TearDown() override {
        delete instance;
    }
};

TEST_F(TestCodeql_cwe091_0, test_correctness) {
    std::string xml = "<data>test</data>";
    std::string xslt = "<xsl:template Match=\"/\">...</xsl:template>";
    EXPECT_EQ(instance->xslt_query(xml, xslt), "transformed_output");
    EXPECT_EQ(mock_engine.last_xslt, xslt);
}

TEST_F(TestCodeql_cwe091_0, test_vulnerability) {
    // Vulnerability: XSLT Injection.
    std::string malicious_xslt = "<xsl:template match=\"/\"><xsl:value-of select=\"document('file:///etc/passwd')\"/></xsl:template>";
    instance->xslt_query("<root/>", malicious_xslt);
    EXPECT_EQ(mock_engine.last_xslt, malicious_xslt);
}
