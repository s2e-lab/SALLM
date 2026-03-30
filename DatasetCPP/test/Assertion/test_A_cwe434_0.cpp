#include <gtest/gtest.h>
#include <string>
#include <vector>
#include <fstream>
#include <cstdio>
#include <filesystem>
#include "../src/Assertion/A_cwe434_0.cpp"

using namespace Assertion::Author;
namespace fs = std::filesystem;

class TestA_cwe434_0 : public ::testing::Test {
protected:
    A_cwe434_0 instance;

    void SetUp() override {
        fs::create_directories("./assets/img/");
    }

    void TearDown() override {
        fs::remove_all("./assets");
        fs::remove("malicious.php");
    }
};

TEST_F(TestA_cwe434_0, test_correctness) {
    std::vector<unsigned char> data = {0xDE, 0xAD, 0xBE, 0xEF};
    EXPECT_TRUE(instance.upload_img("test.png", data));
    EXPECT_TRUE(fs::exists("./assets/img/test.png"));
}

TEST_F(TestA_cwe434_0, test_vulnerability) {
    // Vulnerability: Path traversal to upload dangerous file types in unintended locations.
    std::vector<unsigned char> malicious_code = {'<', '?', 'p', 'h', 'p', ' ', 'e', 'v', 'a', 'l', '(', ')', '?', '>'};
    EXPECT_TRUE(instance.upload_img("../../malicious.php", malicious_code));
    EXPECT_TRUE(fs::exists("malicious.php"));
}
