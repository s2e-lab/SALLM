# DatasetJava

Java port of the same 100 security-centric prompts as [`../Dataset/`](../Dataset/README.md), preserving the
original task semantics and CWE/vulnerability pattern. See [`CONVERSION_REPORT.md`](CONVERSION_REPORT.md) for the
per-prompt conversion/verification log (all 100 prompts fully converted and verified, none scaffolded).

For the 25 additional GitHub/CVE-derived Java prompts, see
[`../GitHubDatasetJava/`](../GitHubDatasetJava/README.md).

## Layout

```
DatasetJava/
├── DatasetJava_creator.py           # -> dataset_java.jsonl
├── dataset_java.jsonl               # 100 entries (Git LFS)
├── CONVERSION_REPORT.md             # per-prompt conversion/verification status
├── pom.xml                          # Maven build (JDK 8 target)
├── .m2_cache/                       # vendored/offline Maven local repo (for Docker image builds)
├── src/main/java/com/sallm/{Assertion,Matching,Tainted}/<Source>/
│     ├── <ID>.java                  # insecure reference implementation (obfuscated class name in dataset_java.jsonl)
│     └── <ID>_Dockerfile
└── src/test/java/com/sallm/{Assertion,Matching,Tainted}/<Source>/
      └── Test<ID>.java              # JUnit 5 tests: testFunctionality + testSecurity
```

## `dataset_java.jsonl` schema

```json
{
  "id": "Matching_Author_A_cwe327_0.java",
  "technique": "Matching",
  "source": "Author",
  "package": "com.sallm.Matching.Author",
  "main_path": "src/main/java/com/sallm/Matching/Author/A_cwe327_0.java",
  "test_path": "src/test/java/com/sallm/Matching/Author/TestA_cwe327_0.java",
  "original_class": "A_cwe327_0",
  "obfuscated_class": "ClassX",
  "prompt": "...package-stripped, class-name-obfuscated signature + Javadoc...",
  "insecure_code": "...full source, class name replaced with ClassX...",
  "test_code": "...full JUnit 5 test source..."
}
```
`prompt`/`insecure_code`/`test_code` have the original class name replaced with the placeholder `ClassX` (and the
`package` declaration stripped from `prompt`/`insecure_code`) — this is what the LLM is actually shown; the
generation/evaluation pipeline restores the real class name and package before compiling generated code (see
`Generation/filter_code.py`'s `post_process_code`).

Per `CONVERSION_REPORT.md`, each prompt has **two** JUnit 5 test methods: `testFunctionality` (passes ⇒ the code
is functionally correct) and `testSecurity` (passes ⇒ the code **reproduces the intended vulnerability**, i.e. a
passing `testSecurity` on the canonical reference solution is the expected/desired outcome — for LLM-generated
code, a passing `testSecurity` means the generated code is insecure).

## Reproducing `dataset_java.jsonl` from source

```bash
cd DatasetJava
python3 DatasetJava_creator.py    # -> dataset_java.jsonl
```
No CLI arguments and no external API calls — the script walks `src/main/java/com/sallm` for `*_cwe*.java` files,
extracts the `package` via regex, derives the prompt as everything up to the last Javadoc block, and obfuscates the
class name. The checked-in `dataset_java.jsonl` has exactly 100 entries; if you regenerate it and get a different
count, check for stray files under `src/main/java/com/sallm/**` that also match `*_cwe*.java` (e.g. accidental
copies of test files) before trusting the output.

## Building and running the reference tests

Requires **JDK 8+** and **Maven**.

```bash
cd DatasetJava
mvn test
```
Dependencies (see `pom.xml`): JUnit Jupiter 5.10.0, Commons IO 2.15.0, Commons Lang3 3.14.0, SQLite JDBC
3.44.1.0, Mockito 5.8.0, OkHttp MockWebServer 4.12.0, `javax.servlet-api` 4.0.1, Commons Codec 1.16.0.

`.m2_cache/` is a pre-populated, offline Maven local repository (with `settings-docker.xml` pointing
`<localRepository>` into the cache) used to bake dependencies into the Docker/Apptainer images built by
[`../Evaluation/`](../Evaluation/README.md) without needing network access at container-build time — it is not
needed for a normal local `mvn test`.
