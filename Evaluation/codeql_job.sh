rm -rf ./CodeQL_Result/gpt-4_0.8
mkdir -p ./CodeQL_Result/gpt-4_0.8

cd ./Dataset/gpt-4_0.8

rm -rf /tmp/msiddiq3/CodeQL_Database/gpt-4_0.8
mkdir -p /tmp/msiddiq3/CodeQL_Database/gpt-4_0.8
codeql database create /tmp/msiddiq3/CodeQL_Database/gpt-4_0.8 --language=python

codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/experimental/Security/ --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_experimental_security.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/experimental/cryptography/ --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_experimental_cryptography.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-020-ExternalAPIs --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_020_externalAPIS.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-020 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_020.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-022 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_022.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-078 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_078.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-079 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_079.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-089 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_089.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-090 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_090.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-094 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_094.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-116 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_116.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-117 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_117.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-209 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_209.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-215 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_215.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-285 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_285.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-295 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_295.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-312 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_312.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-326 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_326.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-327 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_327.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-352 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_352.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-377 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_377.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-502 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_502.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-601 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_601.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-611 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_611.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-643 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_643.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-730 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_730.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-732 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_732.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-776 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_776.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-798 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_798.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-918 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_918.csv"
codeql database analyze "/tmp/msiddiq3/CodeQL_Database/gpt-4_0.8" /afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql-repo/python/ql/src/Security/CWE-943 --format=csv --output="../../CodeQL_Result/gpt-4_0.8/results_cwe_943.csv"


rm -rf Dataset/gpt-4_0.8
# mkdir Dataset