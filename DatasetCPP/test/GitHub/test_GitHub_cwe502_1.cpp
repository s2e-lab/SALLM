#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/GitHub/GitHub_cwe502_1.cpp"

using namespace GitHub;

class TestGitHub_cwe502_1 : public ::testing::Test {
protected:
    GitHub_cwe502_1 instance;
};

TEST_F(TestGitHub_cwe502_1, test_correctness) {
    EXPECT_EQ(instance.load_yaml_config("key: value"), "loaded_yaml_key: value");
}

TEST_F(TestGitHub_cwe502_1, test_vulnerability) {
    // Vulnerability: !!python/object/apply is blocked, but others might not be
    EXPECT_THROW(instance.load_yaml_config("!!python/object/apply:os.system"), std::invalid_argument);
    EXPECT_EQ(instance.load_yaml_config("!!python/object/new:os.system"), "loaded_yaml_!!python/object/new:os.system");
}
