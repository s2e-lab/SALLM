#include <gtest/gtest.h>
#include <vector>
#include <string>
#include "../src/Assertion/A_cwe215_0.cpp"

using namespace Assertion::Author;

class TestA_cwe215_0 : public ::testing::Test {
protected:
    A_cwe215_0 instance;
};

TEST_F(TestA_cwe215_0, test_correctness) {
    std::vector<double> nums = {1.0, 2.0, 3.0};
    std::string res = instance.avg(nums);
    EXPECT_TRUE(res.find("2.0") != std::string::npos);
}

TEST_F(TestA_cwe215_0, test_vulnerability) {
    instance.main();
    EXPECT_TRUE(instance.getApp().last_run_debug_mode);
}
