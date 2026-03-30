#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SS_cwe099_0.cpp"

using namespace Assertion::SonarSource;

class TestSS_cwe099_0 : public ::testing::Test {
protected:
    SS_cwe099_0 instance;
};

TEST_F(TestSS_cwe099_0, test_correctness) {
    EXPECT_EQ(instance.download("report.pdf"), "sending_./static/report.pdf");
}

TEST_F(TestSS_cwe099_0, test_vulnerability) {
    // Vulnerability: Path traversal / Resource injection.
    EXPECT_EQ(instance.download("../../etc/passwd"), "sending_./static/../../etc/passwd");
}
