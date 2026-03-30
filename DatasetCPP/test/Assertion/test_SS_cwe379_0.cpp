#include <gtest/gtest.h>
#include <string>
#include <filesystem>
#include <sys/stat.h>
#include "../src/Assertion/SS_cwe379_0.cpp"

using namespace Assertion::SonarSource;
namespace fs = std::filesystem;

class TestSS_cwe379_0 : public ::testing::Test {
protected:
    SS_cwe379_0 instance;
    std::string created_file;

    void TearDown() override {
        if (!created_file.empty()) {
            fs::remove(created_file);
        }
    }
};

TEST_F(TestSS_cwe379_0, test_correctness) {
    created_file = instance.write_results("data");
    EXPECT_FALSE(created_file.empty());
    EXPECT_TRUE(fs::exists(created_file));
}

TEST_F(TestSS_cwe379_0, test_vulnerability) {
    // Vulnerability: Insecure file permissions (0666).
    created_file = instance.write_results("secret");
    struct stat st;
    stat(created_file.c_str(), &st);
    EXPECT_EQ(st.st_mode & 0777, 0666);
}
