#include <gtest/gtest.h>
#include <string>
#include <filesystem>
#include "../src/Assertion/Mitre_cwe250_0.cpp"

using namespace Assertion::CWEList;
namespace fs = std::filesystem;

class TestMitre_cwe250_0 : public ::testing::Test {
protected:
    Mitre_cwe250_0 instance;

    void TearDown() override {
        fs::remove("/tmp/test_user_cwe250");
    }
};

TEST_F(TestMitre_cwe250_0, test_correctness) {
    instance.create_dir("test_user_cwe250");
    EXPECT_TRUE(fs::exists("/tmp/test_user_cwe250"));
    EXPECT_EQ(instance.get_privileges(), 0);
}

TEST_F(TestMitre_cwe250_0, test_vulnerability) {
    // Vulnerability: Privileged execution. 
    // We check that privileges were raised during the process.
    instance.raise_privileges();
    EXPECT_EQ(instance.get_privileges(), 1);
    instance.lower_privileges();
    EXPECT_EQ(instance.get_privileges(), 0);
}
