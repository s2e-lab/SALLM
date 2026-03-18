"""
generate_test_figures.py

Converts tests_result.ipynb for both Java and Python datasets.

Reads:
  ../Evaluation/Result/Tests_Results_Java.csv
  ../Evaluation/Result/Tests_Results_Python.csv

Writes Figure/ plots for vul@k, security@k, pass@k (per dataset).
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
RESULT_DIR = os.path.join(BASE_DIR, "..", "Evaluation", "Result")
FIG_DIR    = os.path.join(BASE_DIR, "Figure")
os.makedirs(FIG_DIR, exist_ok=True)

MODEL_LABELS = {
    "gpt":       "GPT-4o-Mini",
    "gemini":    "Gemini-2.5-Flash",
    "Qwen":      "Qwen-2.5-Coder",
    "starcoder": "Starcoder-2",
}


def pretty_model(name):
    for key, label in MODEL_LABELS.items():
        if key in name:
            return label
    return name


def plot_metric(df, metric_col, ylabel, suffix, fig_name):
    cols = 5
    languages = df["Language"].unique()
    rows = (len(languages) + cols - 1) // cols

    fig, axs = plt.subplots(rows, cols, figsize=(12, 2 * rows),
                            sharex=True, sharey=True, dpi=300)
    axs_flat = axs.flatten()

    for idx, lang in enumerate(languages):
        ax = axs_flat[idx]
        subset = df[df["Language"] == lang]
        for model in subset["Model"].unique():
            mdata = subset[subset["Model"] == model]
            label = pretty_model(model)
            ax.plot(mdata["Temp"], mdata[f"{metric_col}@1"],
                    label=f"{label} - @1", linestyle="-",  marker="o")
            ax.plot(mdata["Temp"], mdata[f"{metric_col}@3"],
                    label=f"{label} - @3", linestyle="--", marker="x")
            ax.plot(mdata["Temp"], mdata[f"{metric_col}@5"],
                    label=f"{label} - @5", linestyle=":",  marker="s")

        ax.set_ylim(0, 100)
        ax.set_title(lang)
        ax.set_xlabel("Temperature")
        ax.set_ylabel(ylabel)
        if idx % cols != 0:
            ax.set_ylabel("")
            ax.tick_params(labelleft=False)
        if idx < (rows - 1) * cols:
            ax.set_xlabel("")
            ax.tick_params(labelbottom=False)
        ax.grid(True)

    for j in range(idx + 1, len(axs_flat)):
        fig.delaxes(axs_flat[j])

    handles, labels = axs_flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower right", ncol=2, fontsize="small")
    plt.tight_layout()
    fig.subplots_adjust(bottom=0.1)

    out = os.path.join(FIG_DIR, fig_name)
    plt.savefig(out, dpi=300)
    plt.close(fig)
    print(f"  Saved {out}")


def process(csv_path, suffix):
    if not os.path.exists(csv_path):
        print(f"  WARNING: {csv_path} not found — skipping {suffix}")
        return
    df = pd.read_csv(csv_path)
    df = df.sort_values(["Model", "Temp", "Language"])
    df["Temp"] = df["Temp"].astype(float)

    plot_metric(df, "vul",      "Vulnerable@k (%)", suffix, f"tests_vul_at_k_comparison_{suffix}.png")
    plot_metric(df, "security", "Security@k (%)",   suffix, f"tests_security_at_k_comparison_{suffix}.png")
    plot_metric(df, "pass",     "Pass@k (%)",        suffix, f"tests_pass_at_k_comparison_{suffix}.png")


def main():
    print("[tests] Java …")
    process(os.path.join(RESULT_DIR, "Tests_Results_Java.csv"),   "java")
    print("[tests] Python …")
    process(os.path.join(RESULT_DIR, "Tests_Results_Python.csv"), "python")


if __name__ == "__main__":
    main()
