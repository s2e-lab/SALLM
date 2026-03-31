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
    low_name = name.lower()
    for key, label in MODEL_LABELS.items():
        if key.lower() in low_name:
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
    n_cols = 1  # Combined into 1 column
    ref_df = next(d for _, d in datasets if d is not None)
    temps  = sorted(ref_df["Temp"].unique())

    fig, axs = plt.subplots(n_rows, n_cols,
                            figsize=(6.0 * n_cols, 4.0 * n_rows),
                            sharex=True, sharey=False, dpi=200)
    axs = np.array(axs).reshape(n_rows, n_cols)

    row_idx = 0
    for lang_label, df in datasets:
        if df is None:
            continue
        ax = axs[row_idx, 0]
        for model in models:
            mdf = df[df["Model"] == model]
            if mdf.empty:
                continue
            
            color = MODEL_COLORS.get(model, None)
            
            # Plot After repair (Solid)
            grp_after  = mdf.groupby("Temp")["Compilable_after (%)"]
            mean_after = grp_after.mean()
            std_after  = grp_after.std().fillna(0)
            t          = mean_after.index.values
            ax.plot(t, mean_after.values, marker="o", label=f"{model} (After)",
                    color=color, linewidth=1.8, markersize=5, linestyle="-")
            ax.fill_between(t, (mean_after - std_after).values, (mean_after + std_after).values,
                            alpha=0.1, color=color)

            # Plot Before repair (Dashed, same color)
            grp_before  = mdf.groupby("Temp")["Compilable_before (%)"]
            mean_before = grp_before.mean()
            ax.plot(t, mean_before.values, marker="x", label=f"{model} (Before)",
                    color=color, linewidth=1.2, markersize=4, linestyle="--", alpha=0.7)

        ax.set_xlim(temps[0] - 0.05, temps[-1] + 0.05)
        ax.set_ylim(0, 100)
        ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
        ax.set_xticks(temps)
        ax.tick_params(axis="x", labelsize=8, rotation=45)
        ax.set_ylabel(f"{lang_label}\nCompilable (%)", fontsize=9)
        
        if row_idx == 0:
            ax.set_title("Compilation Rate: Before vs After Repair", fontsize=11, fontweight="bold")
        if row_idx == n_rows - 1:
            ax.set_xlabel("Temperature", fontsize=9)
        row_idx += 1

    handles, labels = axs[0, 0].get_legend_handles_labels()
    # Filter legend to avoid clutter? Or show all?
    # Let's show all for now, but formatted
    fig.legend(handles, labels,
               loc="lower center", ncol=2,
               fontsize=8, frameon=True,
               bbox_to_anchor=(0.5, -0.1))
    plt.tight_layout(rect=[0, 0, 1, 1])
    out = os.path.join(FIG_DIR, fig_name)
    plt.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


def plot_nl_compilation_figure(df, ylabel, fig_name):
    """
    6 rows (temperatures) x 4 cols (models).
    x-axis: natural languages (line chart, rotated labels).
    y-axis: compilable (%).
    One figure per programming language (Java/Python/C++).
    """
    models = list(MODEL_LABELS.values())
    temps  = sorted(df["Temp"].unique())
    langs  = sorted(df["Language"].unique())
    x      = np.arange(len(langs))

    n_rows = len(temps)
    n_cols = len(models)

    fig, axs = plt.subplots(n_rows, n_cols,
                            figsize=(5.0 * n_cols, 3.5 * n_rows),
                            sharey=False, dpi=200)
    axs = np.array(axs).reshape(n_rows, n_cols)

    for row_idx, temp in enumerate(temps):
        for col_idx, model in enumerate(models):
            ax  = axs[row_idx, col_idx]
            mdf = df[(df["Model"] == model) & (df["Temp"] == temp)]
            color = MODEL_COLORS.get(model, None)

            # Data for Before repair
            vals_before = []
            for lang in langs:
                ldf = mdf[mdf["Language"] == lang]
                vals_before.append(ldf["Compilable_before (%)"].mean() if not ldf.empty else 0.0)
            
            # Data for After repair
            vals_after = []
            for lang in langs:
                ldf = mdf[mdf["Language"] == lang]
                vals_after.append(ldf["Compilable_after (%)"].mean() if not ldf.empty else 0.0)

            # Plot lines
            # 'After' is solid and thick
            ax.plot(x, vals_after, marker="o", color=color, label="After Repair",
                    linewidth=2.0, markersize=4, linestyle="-", alpha=1.0)
            
            # 'Before' is dashed and thin
            ax.plot(x, vals_before, marker="x", color="gray", label="Before Repair",
                    linewidth=1.2, markersize=3, linestyle="--", alpha=0.7)

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
                ax.set_title(model, fontsize=10, fontweight="bold")
            
    # Add a global legend for the whole figure
    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, fontsize=9, frameon=True, bbox_to_anchor=(0.5, -0.02))

    plt.tight_layout(rect=[0, 0.03, 1, 1])
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

    # Per-natural-language figures: 6 temps x 4 models, x=NL, combined (Before & After)
    nl_datasets = [
        ("Java",   df_java),
        ("Python", df_python),
        ("Cpp",    df_cpp),
    ]
    for prog_label, df in nl_datasets:
        if df is None:
            continue
        fig_name = f"nl_{prog_label}_compilable.png"
        print(f"[nl-compilation] {prog_label} combined comparison …")
        plot_nl_compilation_figure(df, "Compilable (%)", fig_name)


if __name__ == "__main__":
    main()
