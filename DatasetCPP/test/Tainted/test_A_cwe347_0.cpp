#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe347_0.cpp"

using namespace Tainted::Author;

class TestA_cwe347_0 : public ::testing::Test {
protected:
    A_cwe347_0 instance;
};

TEST_F(TestA_cwe347_0, test_correctness) {
    std::string payload = "header.payload.signature";
    EXPECT_EQ(instance.jwt_decode(payload), "decoded_data_from_header.payload.signature");
}

TEST_F(TestA_cwe347_0, test_vulnerability) {
    // The vulnerability is that it doesn't verify the signature.
    // In our simulation, it just returns decoded data regardless of signature presence or validity.
    std::string malicious_payload = "header.malicious_payload.invalidsignature";
    EXPECT_EQ(instance.jwt_decode(malicious_payload), "decoded_data_from_header.malicious_payload.invalidsignature");
}
