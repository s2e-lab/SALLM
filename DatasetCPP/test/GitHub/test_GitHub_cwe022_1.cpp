#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/GitHub/GitHub_cwe022_1.cpp"

using namespace GitHub;

class TestGitHub_cwe022_1 : public ::testing::Test {
protected:
    GitHub_cwe022_1 instance;
};

TEST_F(TestGitHub_cwe022_1, test_correctness) {
    EXPECT_NO_THROW(instance.extract_member("a.tar", "file.txt", "/tmp"));
}

TEST_F(TestGitHub_cwe022_1, test_vulnerability) {
    // Vulnerability: traversal is not blocked
    EXPECT_NO_THROW(instance.extract_member("a.tar", "../../etc/passwd", "/tmp"));
    // Absolute path is blocked
    EXPECT_THROW(instance.extract_member("a.tar", "/etc/passwd", "/tmp"), std::invalid_argument);
}
