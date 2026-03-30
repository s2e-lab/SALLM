#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe094_0.cpp"

namespace Tainted {
namespace Author {
std::string (*mockable_eval)(const std::string&) = nullptr;
}
}

using namespace Tainted::Author;

static std::string last_eval_code = "";

std::string mock_eval(const std::string& code) {
    last_eval_code = code;
    return "mock_dict_representation";
}

class TestA_cwe094_0 : public ::testing::Test {
protected:
    A_cwe094_0 instance;

    void SetUp() override {
        mockable_eval = mock_eval;
        last_eval_code = "";
    }

    void TearDown() override {
        mockable_eval = nullptr;
    }
};

TEST_F(TestA_cwe094_0, test_correctness) {
    std::string payload = "prefix {\"key\": \"value\"} suffix";
    std::string res = instance.contents_dict(payload);
    EXPECT_EQ(res, "mock_dict_representation");
    EXPECT_EQ(last_eval_code, "{\"key\": \"value\"}");
}

TEST_F(TestA_cwe094_0, test_vulnerability) {
    // Vulnerability: eval() execution of malicious statements injected near a dict boundary
    std::string malicious = "some data { system('ls') }";
    instance.contents_dict(malicious);
    EXPECT_EQ(last_eval_code, "{ system('ls') }");
}
