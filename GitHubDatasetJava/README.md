# GitHubDatasetJava

Java port of [`../GitHubDataset/`](../GitHubDataset/README.md)'s 25 real-world/CVE-derived prompts — see that
README for the source/selection criteria. The C++ counterpart lives under `src/GitHub/`/`test/GitHub/` in
[`../DatasetCPP/`](../DatasetCPP/README.md).

## Layout

```
GitHubDatasetJava/
├── generate_java_jsonl.py            # -> github-dataset_java.jsonl
├── github-dataset_java.jsonl         # 25 entries (Git LFS)
├── pom.xml
├── src/main/java/com/sallm/GitHub/GitHub/*.java        # insecure reference implementations
└── src/test/java/com/sallm/GitHub/GitHub/Test*.java    # JUnit 5 tests
```

## `github-dataset_java.jsonl` schema

Same shape as [`../DatasetJava/dataset_java.jsonl`](../DatasetJava/README.md), plus a `language` field:
`id, technique ("GitHub"), source ("GitHub"), package, main_path, test_path, original_class, obfuscated_class,
prompt, insecure_code, test_code, language ("Java")`.

## Reproducing `github-dataset_java.jsonl`

```bash
cd GitHubDatasetJava
python3 generate_java_jsonl.py
```
**Before running**, edit the `DATASET_ROOT` constant near the top of `generate_java_jsonl.py` — it is hard-coded to
the original author's local absolute path and must point at your own checkout of this `GitHubDatasetJava/`
directory. No other CLI arguments are needed, and there are no external API calls.

## Building and running the reference tests

Requires JDK 8+ and Maven:
```bash
cd GitHubDatasetJava
mvn test
```
Dependencies mirror [`../DatasetJava/pom.xml`](../DatasetJava/README.md) with one addition
(`org.yaml:snakeyaml:2.2`, for YAML-deserialization CVE samples) and one version difference worth knowing about if
you see inconsistent Mockito behavior across the two Java modules: `mockito-core` is pinned to **4.11.0** here vs.
**5.8.0** in `DatasetJava/pom.xml`.
