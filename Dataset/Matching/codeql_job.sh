rm -rf CodeQL_Database
mkdir CodeQL_Database
codeql database create ./CodeQL_Database --language=python

rm -rf CodeQL_Result
mkdir CodeQL_Result
codeql database analyze "./CodeQL_Database" /Users/codeql-home/codeql-repo/python/ql/src/experimental/Security/ --format=csv --output="./CodeQL_Result/results_experimental_security.csv"
codeql database analyze "./CodeQL_Database" /Users/codeql-home/codeql-repo/python/ql/src/experimental/cryptography/ --format=csv --output="./CodeQL_Result/results_experimental_cryptography.csv"
codeql database analyze "./CodeQL_Database" /Users/codeql-home/codeql-repo/python/ql/src/Security/CWE-078 --format=csv --output="./CodeQL_Result/results_cwe_078.csv"
codeql database analyze "./CodeQL_Database" /Users/codeql-home/codeql-repo/python/ql/src/Security/CWE-327 --format=csv --output="./CodeQL_Result/results_cwe_327.csv"
codeql database analyze "./CodeQL_Database" /Users/codeql-home/codeql-repo/python/ql/src/Security/CWE-377 --format=csv --output="./CodeQL_Result/results_cwe_377.csv"
codeql database analyze "./CodeQL_Database" /Users/codeql-home/codeql-repo/python/ql/src/Security/CWE-502 --format=csv --output="./CodeQL_Result/results_cwe_502.csv"