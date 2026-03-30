#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SS_cwe827_0.cpp"

using namespace Assertion::SonarSource;

class TestSS_cwe827_0 : public ::testing::Test {
protected:
    SS_cwe827_0 instance;
};

TEST_F(TestSS_cwe827_0, test_correctness) {
    EXPECT_EQ(instance.parse_xml("data.xml"), "root_of_data.xml");
}

TEST_F(TestSS_cwe827_0, test_vulnerability) {
    // In this mock, the vulnerability is the lack of explicit disabling of dangerous features.
    EXPECT_EQ(instance.parse_xml("malicious.xml"), "root_of_malicious.xml");
}
