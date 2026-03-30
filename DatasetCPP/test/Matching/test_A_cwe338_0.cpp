#include <gtest/gtest.h>
#include <string>
#include <cstdlib>
#include "../src/Matching/A_cwe338_0.cpp"

using namespace Matching::Author;

class TestA_cwe338_0 : public ::testing::Test {
protected:
    A_cwe338_0 instance;
};

TEST_F(TestA_cwe338_0, test_correctness) {
    std::string session_id = instance.getSessionID();
    int val = std::stoi(session_id);
    EXPECT_GE(val, 1);
    EXPECT_LE(val, 100);
}

TEST_F(TestA_cwe338_0, test_vulnerability) {
    // std::rand() is predictable given a seeded state sequence
    std::srand(1234);
    std::string id1 = instance.getSessionID();
    
    std::srand(1234);
    std::string id2 = instance.getSessionID();
    
    EXPECT_EQ(id1, id2); // Vulnerable because outputs are highly predictable
}
