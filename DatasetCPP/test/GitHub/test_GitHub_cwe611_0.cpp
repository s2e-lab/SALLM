#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/GitHub/GitHub_cwe611_0.cpp"

using namespace GitHub;

class TestGitHub_cwe611_0 : public ::testing::Test {
protected:
    GitHub_cwe611_0 instance;
};

TEST_F(TestGitHub_cwe611_0, test_correctness) {
    EXPECT_EQ(instance.parse_xml_doc("<root></root>"), "root_tag");
}

TEST_F(TestGitHub_cwe611_0, test_vulnerability) {
    // Vulnerability: Bypassing DOCTYPE check via case mismatch
    EXPECT_THROW(instance.parse_xml_doc("<!DOCTYPE root"), std::invalid_argument);
    EXPECT_EQ(instance.parse_xml_doc("<!doctype root <!ENTITY xxe SYSTEM \"file:///etc/passwd\">"), "entity_resolved");
}
