#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <filesystem>
#include "../src/Assertion/SE_cwe022_0.cpp"

using namespace Assertion::SecurityEval;
namespace fs = std::filesystem;

class TestSE_cwe022_0 : public ::testing::Test {
protected:
    SE_cwe022_0 instance;

    void SetUp() override {
        std::ofstream file("image.png");
        file << "data";
        file.close();
    }

    void TearDown() override {
        fs::remove("image.png");
        fs::remove("../dangerous.txt");
    }
};

TEST_F(TestSE_cwe022_0, test_correctness) {
    instance.delateImage("image.png");
    EXPECT_FALSE(fs::exists("image.png"));
}

TEST_F(TestSE_cwe022_0, test_vulnerability) {
    // Vulnerability: Path traversal allowing deletion of files outside the intended directory.
    std::ofstream file("../dangerous.txt");
    file << "sensitive";
    file.close();
    
    instance.delateImage("../dangerous.txt");
    EXPECT_FALSE(fs::exists("../dangerous.txt"));
}
