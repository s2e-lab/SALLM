#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe116_0.cpp"

using namespace GitHub;

class TestGitHub_cwe116_0 : public ::testing::Test {
protected:
    GitHub_cwe116_0 instance;
};

TEST_F(TestGitHub_cwe116_0, test_correctness) {
    EXPECT_EQ(instance.clean_input("safe<script>text"), "safetext");
}

TEST_F(TestGitHub_cwe116_0, test_vulnerability) {
    // Vulnerability: Case sensitivity bypass or nested tag bypass
    EXPECT_EQ(instance.clean_input("<SCRIPT>alert(1)</SCRIPT>"), "<SCRIPT>alert(1)</SCRIPT>");
    EXPECT_EQ(instance.clean_input("<sc<script>ript>"), "<script>");
}
