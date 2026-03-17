#!/bin/bash
source /afs/crc.nd.edu/x86_64_linux/Modules/4.7.0/init/bash
module load python/3.12.12
export PATH="/groups/jdasilv2/Latif/codeql-home/codeql:$PATH"
export CODEQL_JAVA_EXTRACTOR_OPTS="-Xmx32G -Xss16M"
rm -rf ./CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0
mkdir -p ./CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0

echo "Created CodeQL Output Directory"

cd ./Dataset/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0

echo "Changed Directory to Dataset/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0"

# Ensure fresh database
rm -rf /tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0
mkdir -p /tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0
codeql database create /tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0 \
    --language=java \
    --ram=32768 \
    -Ojava.buildless=true \
    -Ojava.buildless.fetch-dependencies=false \
    -Obuildless.fetch-dependencies=false \
    -Ojava.buildless.annotation-processors=false \
    --skip-empty \
    --verbose

echo "Finalizing CodeQL Database"
codeql database finalize /tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0

echo "Created CodeQL Database"

# Experimental Queries
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-020 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-020.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-078 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-078.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-089 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-089.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-094 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-094.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-208 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-208.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-295 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-295.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-327 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-327.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-352 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-352.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-502 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-502.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/experimental/Security/CWE/CWE-601 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_experimental_CWE-601.csv"

# Security Queries
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-020 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_020.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-022 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_022.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-074 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_074.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-078 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_078.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-079 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_079.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-089 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_089.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-090 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_090.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-094 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_094.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-113 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_113.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-117 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_117.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-129 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_129.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-134 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_134.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-190 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_190.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-200 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_200.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-209 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_209.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-295 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_295.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-297 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_297.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-312 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_312.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-319 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_319.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-326 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_326.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-327 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_327.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-338 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_338.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-352 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_352.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-367 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_367.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-470 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_470.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-489 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_489.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-501 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_501.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-502 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_502.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-522 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_522.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-532 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_532.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-601 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_601.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-611 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_611.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-614 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_614.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-643 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_643.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-730 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_730.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-732 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_732.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-798 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_798.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-807 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_807.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-917 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_917.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-918 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_918.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0" /groups/jdasilv2/Latif/codeql-home/codeql-repo/java/ql/src/Security/CWE/CWE-927 --format=csv --output="../../CodeQL_Output/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0/results_cwe_927.csv"

# Cleanup if needed
# rm -rf /groups/jdasilv2/Latif/SALLM/Evaluation/Dataset/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0
# rm -rf /tmp/msiddiq3/CodeQL_Database/dataset_java_nl_prompt_best_gemini-2.5-flash_1.0

echo "Removed Dataset and CodeQL Database"