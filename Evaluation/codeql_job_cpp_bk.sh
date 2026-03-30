#!/bin/bash
source /afs/crc.nd.edu/x86_64_linux/Modules/4.7.0/init/bash
module load python/3.12.12
export PATH="/groups/jdasilv2/Latif/codeql-home/codeql:$PATH"

rm -rf ./CodeQL_Output/MODEL_NAME
mkdir -p ./CodeQL_Output/MODEL_NAME

echo "Created CodeQL Output Directory"

# Ensure fresh database
rm -rf /tmp/msiddiq3/CodeQL_Database/MODEL_NAME
mkdir -p /tmp/msiddiq3/CodeQL_Database/MODEL_NAME

SOURCE_DIR="$(pwd)/Dataset/MODEL_NAME"

# Write build command to a temp script — avoids CodeQL splitting the command
# by spaces instead of passing it through a shell
BUILD_SCRIPT=$(mktemp /tmp/codeql_cpp_build_XXXXXX.sh)
cat > "$BUILD_SCRIPT" << BUILDEOF
#!/bin/bash
find "$SOURCE_DIR" -name '*.cpp' -exec g++ -std=c++17 -fsyntax-only {} \; 2>/dev/null
exit 0
BUILDEOF
chmod +x "$BUILD_SCRIPT"

codeql database create /tmp/msiddiq3/CodeQL_Database/MODEL_NAME \
    --language=cpp \
    --source-root="$SOURCE_DIR" \
    --command="$BUILD_SCRIPT" \
    --ram=32768

rm -f "$BUILD_SCRIPT"

echo "Created CodeQL Database"

CODEQL_REPO=/groups/jdasilv2/Latif/codeql-home/codeql-repo/cpp/ql/src/Security/CWE
OUT=../../CodeQL_Output/MODEL_NAME
DB=/tmp/msiddiq3/CodeQL_Database/MODEL_NAME

codeql database analyze "$DB" $CODEQL_REPO/CWE-020 --format=csv --output="$OUT/results_cwe_020.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-022 --format=csv --output="$OUT/results_cwe_022.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-078 --format=csv --output="$OUT/results_cwe_078.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-079 --format=csv --output="$OUT/results_cwe_079.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-089 --format=csv --output="$OUT/results_cwe_089.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-134 --format=csv --output="$OUT/results_cwe_134.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-190 --format=csv --output="$OUT/results_cwe_190.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-295 --format=csv --output="$OUT/results_cwe_295.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-319 --format=csv --output="$OUT/results_cwe_319.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-326 --format=csv --output="$OUT/results_cwe_326.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-327 --format=csv --output="$OUT/results_cwe_327.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-611 --format=csv --output="$OUT/results_cwe_611.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-732 --format=csv --output="$OUT/results_cwe_732.csv"
codeql database analyze "$DB" $CODEQL_REPO/CWE-807 --format=csv --output="$OUT/results_cwe_807.csv"

# Cleanup
rm -rf /tmp/msiddiq3/CodeQL_Database/MODEL_NAME

echo "CodeQL C++ analysis complete for MODEL_NAME"
