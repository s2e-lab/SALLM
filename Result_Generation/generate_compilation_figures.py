"""
generate_compilation_figures.py

Converts compilation_rate.ipynb for both Java and Python datasets.

Reads:
  ../Evaluation/Result/compilation_results_Java.csv
  ../Evaluation/Result/compilation_results_Python.csv

Writes Figure/compilation_results_{Java|Python}.png
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


def process(csv_path, label):
    if not os.path.exists(csv_path):
        print(f"  WARNING: {csv_path} not found — skipping {label}")
        return

    df = pd.read_csv(csv_path)
    unique_languages = df["Language"].unique()
    cols = 5
    rows = (len(unique_languages) + cols - 1) // cols

    fig, axs = plt.subplots(rows, cols, figsize=(12, 2 * rows),
                            sharex=True, sharey=True, dpi=300)
    axs = axs.flatten()

    for idx, language in enumerate(unique_languages):
        ax = axs[idx]
        lang_df = df[df["Language"] == language]
        for model in lang_df["Model"].unique():
            subset = lang_df[lang_df["Model"] == model]
            mlabel = pretty_model(model)
            ax.plot(subset["Temp"], subset["Compilable_before (%)"],
                    marker="o", label=f"{mlabel} - Before")
            ax.plot(subset["Temp"], subset["Compilable_after (%)"],
                    marker="x", linestyle="--", label=f"{mlabel} - After")

        ax.set_title(language)
        ax.set_xlabel("Temperature")
        ax.set_ylabel("Compilable (%)")
        if idx % cols != 0:
            ax.set_ylabel("")
            ax.tick_params(labelleft=False)
        if idx < (rows - 1) * cols:
            ax.set_xlabel("")
            ax.tick_params(labelbottom=False)
        ax.grid(True)

    for j in range(idx + 1, len(axs)):
        fig.delaxes(axs[j])

    handles, labels = axs[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower right", ncol=2, fontsize="medium")
    plt.tight_layout()

    out = os.path.join(FIG_DIR, f"compilation_results_{label}.png")
    plt.savefig(out, dpi=300)
    plt.close(fig)
    print(f"  Saved {out}")


def main():
    print("[compilation] Java …")
    process(os.path.join(RESULT_DIR, "compilation_results_Java.csv"),   "Java")
    print("[compilation] Python …")
    process(os.path.join(RESULT_DIR, "compilation_results_Python.csv"), "Python")


if __name__ == "__main__":
    main()
