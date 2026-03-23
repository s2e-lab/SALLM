"""
generate_compilation_figures.py

2 rows (Java/Python) × 2 cols (Before/After repair), mean ± std across languages.

Reads:
  ../Evaluation/Result/compilation_results_Java.csv
  ../Evaluation/Result/compilation_results_Python.csv

Writes:
  Figure/compilation_results.png
"""

import os
import numpy as np
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
    "qwen":      "Qwen-2.5-Coder",
    "starcoder": "StarCoder-2",
}

MODEL_COLORS = {
    "GPT-4o-Mini":       "#e07b39",
    "Gemini-2.5-Flash":  "#4878cf",
    "Qwen-2.5-Coder":    "#6acc65",
    "StarCoder-2":       "#d43f3a",
}


def pretty_model(name):
    for key, label in MODEL_LABELS.items():
        if key in name:
            return label
    return name


def load(csv_path):
    if not os.path.exists(csv_path):
        return None
    df = pd.read_csv(csv_path)
    df["Temp"] = df["Temp"].astype(float)
    df["Model"] = df["Model"].apply(pretty_model)
    return df


def plot_compilation(df_java, df_python, fig_name):
    datasets = [("Java", df_java), ("Python", df_python)]
    phases   = [("Before repair", "Compilable_before (%)"),
                ("After repair",  "Compilable_after (%)")]
    models   = list(MODEL_LABELS.values())

    n_rows = sum(1 for _, d in datasets if d is not None)
    n_cols = len(phases)
    ref_df = next(d for _, d in datasets if d is not None)
    temps  = sorted(ref_df["Temp"].unique())

    fig, axs = plt.subplots(n_rows, n_cols,
                            figsize=(4.5 * n_cols, 3.5 * n_rows),
                            sharex=True, sharey=False, dpi=200)
    axs = np.array(axs).reshape(n_rows, n_cols)

    row_idx = 0
    for lang_label, df in datasets:
        if df is None:
            continue
        for col_idx, (phase_label, col) in enumerate(phases):
            ax = axs[row_idx, col_idx]
            for model in models:
                mdf = df[df["Model"] == model]
                if mdf.empty:
                    continue
                grp   = mdf.groupby("Temp")[col]
                mean  = grp.mean()
                std   = grp.std().fillna(0)
                t     = mean.index.values
                color = MODEL_COLORS.get(model, None)
                ax.plot(t, mean.values, marker="o", label=model,
                        color=color, linewidth=1.8, markersize=5)
                ax.fill_between(t,
                                (mean - std).values,
                                (mean + std).values,
                                alpha=0.15, color=color)
            ax.set_xlim(temps[0] - 0.05, temps[-1] + 0.05)
            ax.set_ylim(0, 100)
            ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
            ax.set_xticks(temps)
            ax.tick_params(axis="x", labelsize=8, rotation=45)
            if col_idx == 0:
                ax.set_ylabel(f"{lang_label}\nCompilable (%)", fontsize=9)
            else:
                ax.set_ylabel("")
            if row_idx == 0:
                ax.set_title(phase_label, fontsize=10, fontweight="bold")
            if row_idx == n_rows - 1:
                ax.set_xlabel("Temperature", fontsize=9)
        row_idx += 1

    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels,
               loc="lower center", ncol=len(models),
               fontsize=9, frameon=True,
               bbox_to_anchor=(0.5, -0.04))
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    out = os.path.join(FIG_DIR, fig_name)
    plt.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


def main():
    df_java   = load(os.path.join(RESULT_DIR, "compilation_results_Java.csv"))
    df_python = load(os.path.join(RESULT_DIR, "compilation_results_Python.csv"))

    if df_java is None and df_python is None:
        print("ERROR: no compilation CSVs found.")
        return

    print("[compilation] combined …")
    plot_compilation(df_java, df_python, "compilation_results.png")
    print("[compilation] java …")
    plot_compilation(df_java, None,      "compilation_results_java.png")
    print("[compilation] python …")
    plot_compilation(None,    df_python, "compilation_results_python.png")


if __name__ == "__main__":
    main()
