"""
generate_compilation_figures.py

N rows (Java/Python/C++) × 2 cols (Before/After repair), mean ± std across languages.

Reads:
  ../Evaluation/Result/compilation_results_Java.csv
  ../Evaluation/Result/compilation_results_Python.csv
  ../Evaluation/Result/compilation_results_Cpp.csv

Writes:
  Figure/compilation_results.png
  Figure/compilation_results_java.png
  Figure/compilation_results_python.png
  Figure/compilation_results_cpp.png
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


def plot_compilation(datasets, fig_name):
    """datasets: list of (label, df) pairs; None dfs are skipped."""
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


def plot_nl_compilation_figure(df, phase_col, ylabel, fig_name):
    """
    6 rows (temperatures) x 4 cols (models).
    x-axis: natural languages (bar chart, rotated labels).
    y-axis: compilable (%).
    One figure per (programming language x phase).
    """
    models = list(MODEL_LABELS.values())
    temps  = sorted(df["Temp"].unique())
    langs  = sorted(df["Language"].unique())
    x      = np.arange(len(langs))

    n_rows = len(temps)
    n_cols = len(models)

    fig, axs = plt.subplots(n_rows, n_cols,
                            figsize=(4.5 * n_cols, 3.0 * n_rows),
                            sharey=False, dpi=200)
    axs = np.array(axs).reshape(n_rows, n_cols)

    for row_idx, temp in enumerate(temps):
        for col_idx, model in enumerate(models):
            ax  = axs[row_idx, col_idx]
            mdf = df[(df["Model"] == model) & (df["Temp"] == temp)]
            color = MODEL_COLORS.get(model, None)

            vals = []
            for lang in langs:
                ldf = mdf[mdf["Language"] == lang]
                vals.append(ldf[phase_col].mean() if not ldf.empty else 0.0)

            ax.bar(x, vals, color=color, alpha=0.8)
            ax.set_ylim(0, 100)
            ax.set_xticks(x)
            ax.grid(True, axis="y", linestyle="--", linewidth=0.5, alpha=0.7)

            if row_idx == n_rows - 1:
                ax.set_xticklabels(langs, rotation=90, fontsize=6)
            else:
                ax.set_xticklabels([], fontsize=0)

            if col_idx == 0:
                ax.set_ylabel(f"T={temp:.1f}\n{ylabel}", fontsize=8)
            else:
                ax.set_ylabel("")

            if row_idx == 0:
                ax.set_title(model, fontsize=9, fontweight="bold")

    plt.tight_layout()
    out = os.path.join(FIG_DIR, fig_name)
    plt.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


def main():
    df_java   = load(os.path.join(RESULT_DIR, "compilation_results_Java.csv"))
    df_python = load(os.path.join(RESULT_DIR, "compilation_results_Python.csv"))
    df_cpp    = load(os.path.join(RESULT_DIR, "compilation_results_Cpp.csv"))

    all_datasets = [("Java", df_java), ("Python", df_python), ("C++", df_cpp)]
    if all(d is None for _, d in all_datasets):
        print("ERROR: no compilation CSVs found.")
        return

    print("[compilation] combined …")
    plot_compilation(all_datasets, "compilation_results.png")
    print("[compilation] java …")
    plot_compilation([("Java", df_java)], "compilation_results_java.png")
    print("[compilation] python …")
    plot_compilation([("Python", df_python)], "compilation_results_python.png")
    print("[compilation] cpp …")
    plot_compilation([("C++", df_cpp)], "compilation_results_cpp.png")

    # Per-natural-language figures: 6 temps x 4 models, x=NL, one per (prog_lang, phase)
    nl_datasets = [
        ("Java",   df_java),
        ("Python", df_python),
        ("Cpp",    df_cpp),
    ]
    phases = [
        ("before", "Compilable_before (%)", "Compilable Before Repair (%)"),
        ("after",  "Compilable_after (%)",  "Compilable After Repair (%)"),
    ]
    for prog_label, df in nl_datasets:
        if df is None:
            continue
        for phase_key, phase_col, ylabel in phases:
            fig_name = f"nl_{prog_label}_compilable_{phase_key}.png"
            print(f"[nl-compilation] {prog_label} {phase_key} …")
            plot_nl_compilation_figure(df, phase_col, ylabel, fig_name)


if __name__ == "__main__":
    main()
