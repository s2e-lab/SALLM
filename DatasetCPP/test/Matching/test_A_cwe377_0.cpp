#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <cstdio>
#include "../src/Matching/A_cwe377_0.cpp"

using namespace Matching::Author;

class TestA_cwe377_0 : public ::testing::Test {
protected:
    A_cwe377_0 instance;
};

TEST_F(TestA_cwe377_0, test_correctness) {
    std::string results = "test results";
    std::string path = instance.write_results(results);
    EXPECT_FALSE(path.empty());
    
    std::ifstream f(path);
    std::string content((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());
    EXPECT_EQ(content, results);
    f.close();
    std::remove(path.c_str());
}

TEST_F(TestA_cwe377_0, test_vulnerability) {
    // The vulnerability is the use of an insecure temporary file creation method.
    // We just verify it successfully creates a file path using that method.
    std::string path = instance.write_results("data");
    EXPECT_FALSE(path.empty());
    std::remove(path.c_str());
}
