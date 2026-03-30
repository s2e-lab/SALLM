#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/GitHub/GitHub_cwe502_0.cpp"

using namespace GitHub;

class TestGitHub_cwe502_0 : public ::testing::Test {
protected:
    GitHub_cwe502_0 instance;
};

TEST_F(TestGitHub_cwe502_0, test_correctness) {
    EXPECT_EQ(instance.load_user_data("safe_data"), "unpickled_safe_data");
}

TEST_F(TestGitHub_cwe502_0, test_vulnerability) {
    // Vulnerability: os.system is blocked, but subprocess is not
    EXPECT_THROW(instance.load_user_data("os.system('id')"), std::invalid_argument);
    EXPECT_EQ(instance.load_user_data("subprocess.call(['id'])"), "unpickled_subprocess.call(['id'])");
}
