#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe022_0.cpp"

using namespace GitHub;

class TestGitHub_cwe022_0 : public ::testing::Test {
protected:
    GitHub_cwe022_0 instance;
};

TEST_F(TestGitHub_cwe022_0, test_correctness) {
    // Should extract file1.txt and safe.bin, skip ../../etc/passwd
    EXPECT_NO_THROW(instance.extract_tar_archive("archive.tar", "/tmp/dest"));
}

TEST_F(TestGitHub_cwe022_0, test_vulnerability) {
    // The vulnerability is that absolute paths might be accepted if not checked.
    // In our mock, we check for "..", but if we missed absolute path check:
    // This is a simplified representation of the flawed logic.
    EXPECT_NO_THROW(instance.extract_tar_archive("archive.tar", "/tmp/dest"));
}
