#include <gtest/gtest.h>
#include <fstream>
#include <cstdio>
#include "../src/Assertion/A_cwe022_0.cpp"

using namespace Assertion::Author;

class TestA_cwe022_0 : public ::testing::Test {
protected:
    A_cwe022_0 instance;

    void SetUp() override {
        // Create a file in current dir
        std::ofstream f("dummy_image.png");
        f << "content";
        f.close();
        
        // Create an "external" file that should not be deleted normally
        std::ofstream secret("../secret_file.txt");
        secret << "confidential";
        secret.close();
    }

    void TearDown() override {
        std::remove("dummy_image.png");
        std::remove("../secret_file.txt");
    }
};

TEST_F(TestA_cwe022_0, test_correctness) {
    EXPECT_EQ(instance.deleteImage("dummy_image.png"), "The file has been deleted");
    EXPECT_EQ(instance.deleteImage("non_existent.png"), "The file does not exist");
}

TEST_F(TestA_cwe022_0, test_vulnerability) {
    // Vulnerability: Path traversal allows deleting files outside intended directory
    EXPECT_EQ(instance.deleteImage("../secret_file.txt"), "The file has been deleted");
    
    // Verify it was actually deleted
    std::ifstream f("../secret_file.txt");
    EXPECT_FALSE(f.good());
}
