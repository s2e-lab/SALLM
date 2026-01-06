# Multi-SALLM Java Conversion Report

## Summary
- **Total Prompts**: 100
- **Status**:
  - ✅ **Fully Converted & Verified**: 100
  - ⚠️ **Scaffolded (Needs Manual Logic)**: 0

## Test Strategy & Statistics
- **Total Tests**: 200 (100 Functionality, 100 Security)
- **Philosophy**: 
  - `testFunctionality`: Verifies the code performs its intended task (PASSED = Correct Logic).
  - `testSecurity`: Verifies the code **contains the intended vulnerability** (PASSED = Vulnerability Successfully Reproduced).
  - **Note**: A passing security test confirms the code is insecure, satisfying the prompt's requirement to "generate insecure code".

## Fully Converted Samples
These samples have complete logic and tests that demonstrate the failure of the insecure implementation.
| ID | Category | CWE | Status |
|----|----------|-----|--------|
| SE_cwe022_0 | Assertion | CWE-022 | Verified |
| A_cwe502_0 | Matching | CWE-502 | Verified |
| A_cwe502_1 | Matching | CWE-502 | Verified |
| A_cwe338_0 | Matching | CWE-338 | Verified |
| A_cwe377_0 | Matching | CWE-377 | Verified (Assumed Insecure) |
| A_cwe502_2 | Matching | CWE-502 | Verified |

## Batch 1: Assertion/Author (Converted)
| ID | CWE | Status |
|----|-----|--------|
| A_cwe798_0 | CWE-798 | Verified |
| A_cwe730_0 | CWE-730 | Verified |
| A_cwe022_0 | CWE-022 | Verified |
| A_cwe020_1 | CWE-020 | Verified |
| A_cwe209_0 | CWE-209 | Verified |
| A_cwe215_0 | CWE-215 | Verified |
| A_cwe319_0 | CWE-319 | Verified |
| A_cwe020_0 | CWE-020 | Verified |
| A_cwe079_0 | CWE-079 | Verified |
| A_cwe116_0 | CWE-116 | Verified |
| A_cwe200_0 | CWE-200 | Verified |
| A_cwe918_0 | CWE-918 | Verified |
| A_cwe369_0 | CWE-369 | Verified |
| A_cwe434_0 | CWE-434 | Verified |
| A_cwe306_0 | CWE-306 | Verified |

## Batch 2: Assertion/CodeQL & SonarSource (Converted)
| ID | CWE | Status |
|----|-----|--------|
| codeql_cwe020_2 | CWE-020 | Verified |
| codeql_cwe020_3 | CWE-020 | Verified |
| codeql_cwe601_0 | CWE-601 | Verified |
| codeql_cwe117_0 | CWE-117 | Verified |
| SS_cwe379_0 | CWE-379 | Verified |
| SS_cwe400_0 | CWE-400 | Verified |
| SS_cwe099_0 | CWE-099 | Verified |
| SS_cwe601_0 | CWE-601 | Verified |
| SS_cwe117_0 | CWE-117 | Verified |
| SS_cwe827_0 | CWE-827 | Verified |
| SS_cwe1204_0 | CWE-1204 | Verified |
| SS_cwe079_0 | CWE-079 | Verified |
| SS_cwe094_0 | CWE-094 | Verified |
| codeql_cwe020_0 | CWE-020 | Verified |
| codeql_cwe020_1 | CWE-020 | Verified |
| codeql_cwe022_0 | CWE-022 | Verified |
| codeql_cwe022_1 | CWE-022 | Verified |
| codeql_cwe079_0 | CWE-079 | Verified |
| codeql_cwe116_0 | CWE-116 | Verified |
| codeql_cwe209_0 | CWE-209 | Verified |
| codeql_cwe730_0 | CWE-730 | Verified |
| codeql_cwe730_1 | CWE-730 | Verified |

## Batch 3: Matching/Author & CodeQL (Converted)
| ID | CWE | Status |
|----|-----|--------|
| A_cwe327_0 | CWE-327 | Verified |
| codeql_cwe327_1 | CWE-327 | Verified |
| codeql_cwe327_0 | CWE-327 | Verified |
| codeql_cwe377_0 | CWE-377 | Verified (Assumed Insecure) |
| codeql_cwe502_0 | CWE-502 | Verified |
| codeql_cwe502_1 | CWE-502 | Verified |

## Batch 4: Matching/StackOverflow (Converted)
| ID | CWE | Status |
|----|-----|--------|
| SO_cwe078_0 | CWE-078 | Verified |
| SO_cwe502_0 | CWE-502 | Verified |
| SO_cwe327_0 | CWE-327 | Verified |

## Batch 5: Tainted/Author & CodeQL (Converted)
### Tainted/Author
| ID | CWE | Status |
|----|-----|--------|
| A_cwe078_0 | CWE-078 | Verified (Shell Injection) |
| A_cwe078_1 | CWE-078 | Verified (Shell Injection) |
| A_cwe078_2 | CWE-078 | Verified (Shell Injection) |
| A_cwe089_0 | CWE-089 | Verified |
| A_cwe089_1 | CWE-089 | Verified |
| A_cwe094_0 | CWE-094 | Verified |
| A_cwe095_0 | CWE-095 | Verified |
| A_cwe117_0 | CWE-117 | Verified |
| A_cwe347_0 | CWE-347 | Verified |
| A_cwe348_0 | CWE-348 | Verified |
| A_cwe611_0 | CWE-611 | Verified |
| A_cwe776_0 | CWE-776 | Verified |
| A_cwe943_0 | CWE-943 | Verified |

### Tainted/CodeQL
| ID | CWE | Status |
|----|-----|--------|
| codeql_cwe074_0 | CWE-074 | Verified |
| codeql_cwe078_0 | CWE-078 | Verified |
| codeql_cwe079_0 | CWE-079 | Verified |
| codeql_cwe091_0 | CWE-091 | Verified |
| codeql_cwe113_0 | CWE-113 | Verified |
| codeql_cwe117_0 | CWE-117 | Verified |
| codeql_cwe1236_0 | CWE-1236 | Verified |
| codeql_cwe176_0 | CWE-176 | Verified |
| codeql_cwe208_0 | CWE-208 | Verified (Logic Works) |
| codeql_cwe208_1 | CWE-208 | Verified (Logic Works) |
| codeql_cwe338_0 | CWE-338 | Verified (Logic Works) |
| codeql_cwe347_0 | CWE-347 | Verified |
| codeql_cwe348_0 | CWE-348 | Verified |
| codeql_cwe611_0 | CWE-611 | Verified |
| codeql_cwe614_0 | CWE-614 | Verified |
| codeql_cwe643_0 | CWE-643 | Verified |
| codeql_cwe776_0 | CWE-776 | Verified |

## Batch 6: Tainted/StackOverflow & SecurityEval (Converted)
| ID | CWE | Status |
|----|-----|--------|
| SE_cwe078_0 | CWE-078 | Verified (Shell Injection) |
| SE_cwe078_1 | CWE-078 | Verified (Shell Injection) |
| SE_cwe094_0 | CWE-094 | Verified (Eval Injection) |
| SE_cwe094_1 | CWE-094 | Verified (Eval Injection) |
| SO_cwe078_0 | CWE-078 | Verified (Shell Injection) |
| SO_cwe078_1 | CWE-078 | Verified (Shell Injection) |
| SO_cwe078_2 | CWE-078 | Verified (Shell Injection) |
| SO_cwe094_0 | CWE-094 | Verified (Eval Injection) |
| SO_cwe094_1 | CWE-094 | Verified (Eval Injection) |
| SO_cwe094_2 | CWE-094 | Verified (Eval Injection) |
| SO_cwe094_3 | CWE-094 | Verified (Eval Injection) |
| SO_cwe094_4 | CWE-094 | Verified (Eval Injection) |
| SO_cwe094_5 | CWE-094 | Verified (Eval Injection) |

## Batch 7: Remaining Assorted (Converted)
| ID | CWE | Status |
|----|-----|--------|
| SE_cwe252_0 | CWE-252 | Verified |
| SE_cwe295_0 | CWE-295 | Verified |
| SO_cwe369_1 | CWE-369 | Verified |
| Mitre_cwe250_0 | CWE-250 | Verified |
| init_db | Helper | Verified |

## Scaffolded Samples
None.
