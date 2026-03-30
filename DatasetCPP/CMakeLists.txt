cmake_minimum_required(VERSION 3.14)
project(DatasetCPP CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

include_directories(src test)

# We will collect all implementations into a library.
# We will collect all tests into an executable.

# Collect tests
add_executable(runTests
    test/Assertion/test_A_cwe020_0.cpp
    test/Assertion/test_A_cwe020_1.cpp
    test/Assertion/test_A_cwe022_0.cpp
    test/Assertion/test_A_cwe079_0.cpp
    test/Assertion/test_A_cwe116_0.cpp
    test/Assertion/test_A_cwe200_0.cpp
    test/Assertion/test_A_cwe209_0.cpp
    test/Assertion/test_A_cwe215_0.cpp
    test/Assertion/test_A_cwe306_0.cpp
    test/Assertion/test_A_cwe319_0.cpp
    test/Assertion/test_A_cwe369_0.cpp
    test/Assertion/test_A_cwe434_0.cpp
    test/Assertion/test_A_cwe730_0.cpp
    test/Assertion/test_A_cwe798_0.cpp
    test/Assertion/test_A_cwe918_0.cpp
    test/Assertion/test_codeql_cwe020_0.cpp
    test/Assertion/test_codeql_cwe020_1.cpp
    test/Assertion/test_codeql_cwe020_2.cpp
    test/Assertion/test_codeql_cwe020_3.cpp
    test/Assertion/test_codeql_cwe022_0.cpp
    test/Assertion/test_codeql_cwe022_1.cpp
    test/Assertion/test_codeql_cwe116_0.cpp
    test/Assertion/test_codeql_cwe117_0.cpp
    test/Assertion/test_codeql_cwe209_0.cpp
    test/Assertion/test_codeql_cwe601_0.cpp
    test/Assertion/test_codeql_cwe730_0.cpp
    test/Assertion/test_codeql_cwe730_1.cpp
    test/Assertion/test_Mitre_cwe250_0.cpp
    test/Assertion/test_SE_cwe022_0.cpp
    test/Assertion/test_SE_cwe252_0.cpp
    test/Assertion/test_SE_cwe295_0.cpp
    test/Matching/test_A_cwe327_0.cpp
    test/Matching/test_A_cwe338_0.cpp
    test/Matching/test_A_cwe377_0.cpp
    test/Matching/test_A_cwe502_0.cpp
    test/Matching/test_A_cwe502_1.cpp
    test/Matching/test_A_cwe502_2.cpp
    test/Matching/test_codeql_cwe327_0.cpp
    test/Matching/test_codeql_cwe327_1.cpp
    test/Matching/test_codeql_cwe377_0.cpp
    test/Matching/test_codeql_cwe502_0.cpp
    test/Matching/test_codeql_cwe502_1.cpp
    test/Tainted/test_A_cwe078_0.cpp
    test/Tainted/test_A_cwe078_1.cpp
    test/Tainted/test_A_cwe078_2.cpp
    test/Tainted/test_A_cwe089_0.cpp
    test/Tainted/test_A_cwe089_1.cpp
    test/Tainted/test_A_cwe094_0.cpp
    test/Tainted/test_A_cwe095_0.cpp
    test/Tainted/test_A_cwe117_0.cpp
    test/Tainted/test_A_cwe347_0.cpp
    test/Tainted/test_A_cwe348_0.cpp
    test/Tainted/test_A_cwe611_0.cpp
    test/Tainted/test_A_cwe776_0.cpp
    test/Tainted/test_A_cwe943_0.cpp
    test/Tainted/test_codeql_cwe074_0.cpp
    test/Tainted/test_codeql_cwe078_0.cpp
    test/Tainted/test_codeql_cwe079_0.cpp
    test/Tainted/test_codeql_cwe091_0.cpp
    test/Tainted/test_codeql_cwe113_0.cpp
    test/Tainted/test_codeql_cwe1236_0.cpp
    test/Tainted/test_codeql_cwe176_0.cpp
    test/Tainted/test_codeql_cwe208_0.cpp
    test/Tainted/test_codeql_cwe208_1.cpp
    test/Tainted/test_codeql_cwe338_0.cpp
    test/Tainted/test_codeql_cwe347_0.cpp
    test/Tainted/test_codeql_cwe348_0.cpp
    test/Tainted/test_codeql_cwe611_0.cpp
    test/Tainted/test_codeql_cwe614_0.cpp
    test/Tainted/test_codeql_cwe643_0.cpp
    test/Tainted/test_codeql_cwe776_0.cpp
    test/Tainted/test_SE_cwe078_0.cpp
    test/Tainted/test_SE_cwe078_1.cpp
    test/Tainted/test_SE_cwe094_0.cpp
    test/Tainted/test_SE_cwe094_1.cpp
    test/Tainted/test_SO_cwe078_0.cpp
    test/Tainted/test_SO_cwe078_1.cpp
    test/Tainted/test_SO_cwe078_2.cpp
    test/Tainted/test_SO_cwe094_0.cpp
    test/Tainted/test_SO_cwe094_1.cpp
    test/Tainted/test_SO_cwe094_2.cpp
    test/Tainted/test_SO_cwe094_3.cpp
    test/Tainted/test_SO_cwe094_4.cpp
    test/Tainted/test_SO_cwe094_5.cpp
    test/Matching/test_SO_cwe327_0.cpp
    test/Assertion/test_SO_cwe369_1.cpp
    test/Matching/test_SO_cwe502_0.cpp
    test/Assertion/test_SS_cwe079_0.cpp
    test/Assertion/test_SS_cwe094_0.cpp
    test/Assertion/test_SS_cwe099_0.cpp
    test/Assertion/test_SS_cwe117_0.cpp
    test/Assertion/test_SS_cwe1204_0.cpp
    test/Assertion/test_SS_cwe379_0.cpp
    test/Assertion/test_SS_cwe400_0.cpp
    test/Assertion/test_SS_cwe601_0.cpp
    test/Assertion/test_codeql_cwe079_0.cpp
    test/Tainted/test_codeql_cwe117_0.cpp
    test/Assertion/test_SS_cwe827_0.cpp
    test/Matching/test_SO_cwe078_0.cpp
    test/Assertion/test_A_cwe502_0.cpp
    test/GitHub/test_GitHub_cwe020_0.cpp
    test/GitHub/test_GitHub_cwe020_1.cpp
    test/GitHub/test_GitHub_cwe022_0.cpp
    test/GitHub/test_GitHub_cwe022_1.cpp
    test/GitHub/test_GitHub_cwe078_0.cpp
    test/GitHub/test_GitHub_cwe078_1.cpp
    test/GitHub/test_GitHub_cwe079_0.cpp
    test/GitHub/test_GitHub_cwe079_1.cpp
    test/GitHub/test_GitHub_cwe089_0.cpp
    test/GitHub/test_GitHub_cwe089_1.cpp
    test/GitHub/test_GitHub_cwe094_0.cpp
    test/GitHub/test_GitHub_cwe116_0.cpp
    test/GitHub/test_GitHub_cwe200_0.cpp
    test/GitHub/test_GitHub_cwe200_1.cpp
    test/GitHub/test_GitHub_cwe295_0.cpp
    test/GitHub/test_GitHub_cwe327_0.cpp
    test/GitHub/test_GitHub_cwe327_1.cpp
    test/GitHub/test_GitHub_cwe400_0.cpp
    test/GitHub/test_GitHub_cwe434_0.cpp
    test/GitHub/test_GitHub_cwe502_0.cpp
    test/GitHub/test_GitHub_cwe502_1.cpp
    test/GitHub/test_GitHub_cwe601_0.cpp
    test/GitHub/test_GitHub_cwe611_0.cpp
    test/GitHub/test_GitHub_cwe798_0.cpp
    test/GitHub/test_GitHub_cwe918_0.cpp
)

target_link_libraries(runTests GTest::gtest_main)
include(GoogleTest)
gtest_discover_tests(runTests)

