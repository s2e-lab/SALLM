"""
compare_python_java.py

Reads Tests_Results_Java.csv and Tests_Results_Python.csv, then produces:

  Result/Comparison_pass@1_mean_std_table.csv   (and @3, @5)
  Result/Comparison_vul@1_mean_std_table.csv
  Result/Comparison_security@1_mean_std_table.csv
  Result/Comparison_summary.csv   — per-model mean across all languages/temps

Each comparison table has columns:
  language_family | Model | Java_<metric> | Python_<metric> | Delta (Python-Java)
"""
import os
import pandas as pd

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
RESULT_DIR = os.path.join(BASE_DIR, "Result")

JAVA_CSV   = os.path.join(RESULT_DIR, "Tests_Results_Java.csv")
PYTHON_CSV = os.path.join(RESULT_DIR, "Tests_Results_Python.csv")

LANG_FAMILIES = {
    "Afro-Asiatic":                ["Arabic", "Hebrew"],
    "Austro-Asiatic":              ["Vietnamese"],
    "Austronesian":                ["Indonesian", "Malay", "Tagalog"],
    "Indo-European (Germanic)":    ["English", "Dutch", "German", "Afrikaans"],
    "Indo-European (Romance)":     ["Portuguese", "Spanish", "French", "Italian"],
    "Indo-European (Greek)":       ["Greek"],
    "Indo-European (Iranian)":     ["Persian"],
    "Slavic":                      ["Russian", "Bulgarian"],
    "Sino-Tibetan":                ["Chinese"],
    "Turkic":                      ["Turkish"],
    "Uralic":                      ["Estonian", "Finnish", "Hungarian"],
}
LANG_TO_FAMILY = {lang: fam for fam, langs in LANG_FAMILIES.items() for lang in langs}

METRICS = ["pass@1", "pass@3", "pass@5", "vul@1", "vul@3", "vul@5",
           "security@1", "security@3", "security@5"]


def load(path, label):
    if not os.path.exists(path):
        print(f"WARNING: {path} not found — skipping {label}.")
        return None
    df = pd.read_csv(path)
    df["language_family"] = df["Language"].map(LANG_TO_FAMILY).fillna("Unknown")
    return df


def make_comparison_table(df_java, df_python, metric):
    """Per language-family × Model table with Java, Python, and delta columns."""
    def agg(df, suffix):
        g = (
            df.groupby(["language_family", "Model"])[metric]
            .agg(["mean", "std"])
            .reset_index()
        )
        g["formatted"] = g.apply(
            lambda r: f"{r['mean']:.2f}±{r['std']:.2f}" if pd.notnull(r["std"]) else f"{r['mean']:.2f}±0.00",
            axis=1,
        )
        g["mean_val"] = g["mean"]
        g = g.rename(columns={"formatted": f"{suffix}_{metric}", "mean_val": f"{suffix}_mean"})
        return g[["language_family", "Model", f"{suffix}_{metric}", f"{suffix}_mean"]]

    j = agg(df_java,   "Java")
    p = agg(df_python, "Python")
    merged = j.merge(p, on=["language_family", "Model"], how="outer")

    # Delta = Python mean - Java mean
    merged["Delta (Python-Java)"] = (merged["Python_mean"] - merged["Java_mean"]).round(2)

    return merged[["language_family", "Model",
                   f"Java_{metric}", f"Python_{metric}", "Delta (Python-Java)"]]


def make_summary(df_java, df_python):
    """Per-model mean across all languages/temps for every metric."""
    rows = []
    for model in sorted(set(df_java["Model"].unique()) | set(df_python["Model"].unique())):
        row = {"Model": model}
        for metric in METRICS:
            jv = df_java[df_java["Model"] == model][metric].mean() if model in df_java["Model"].values else float("nan")
            pv = df_python[df_python["Model"] == model][metric].mean() if model in df_python["Model"].values else float("nan")
            row[f"Java_{metric}"]   = round(jv, 3) if pd.notnull(jv) else ""
            row[f"Python_{metric}"] = round(pv, 3) if pd.notnull(pv) else ""
            if pd.notnull(jv) and pd.notnull(pv):
                row[f"Delta_{metric}"] = round(pv - jv, 3)
            else:
                row[f"Delta_{metric}"] = ""
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    df_java   = load(JAVA_CSV,   "Java")
    df_python = load(PYTHON_CSV, "Python")

    if df_java is None or df_python is None:
        print("Cannot generate comparison — one or both result files missing.")
        return

    os.makedirs(RESULT_DIR, exist_ok=True)

    # Per-metric comparison tables
    for metric in METRICS:
        table = make_comparison_table(df_java, df_python, metric)
        out = os.path.join(RESULT_DIR, f"Comparison_{metric}_table.csv")
        table.to_csv(out, index=False)
        print(f"⇒ {out}")

    # Summary
    summary = make_summary(df_java, df_python)
    out = os.path.join(RESULT_DIR, "Comparison_summary.csv")
    summary.to_csv(out, index=False)
    print(f"⇒ {out}")


if __name__ == "__main__":
    main()
