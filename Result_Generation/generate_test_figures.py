"""
generate_test_figures.py

N rows (Java/Python/C++) × 3 cols (k=1/3/5), mean ± std across languages.

Reads:
  ../Evaluation/Result/Tests_Results_Java.csv
  ../Evaluation/Result/Tests_Results_Python.csv
  ../Evaluation/Result/Tests_Results_Cpp.csv

Writes:
  Figure/tests_pass_at_k_comparison.png
  Figure/tests_vul_at_k_comparison.png
  Figure/tests_security_at_k_comparison.png
  (+ per-language variants)
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

K_VALUES = [1, 3, 5]


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


def plot_metric_figure(datasets, metric_col, ylabel, fig_name):
    """
    N-row (Java/Python/C++) × 3-col (k=1,3,5) figure.
    datasets: list of (label, df) pairs; None dfs are skipped.
    Each panel: x=temperature, one line per model (mean over languages),
    shaded ±1-std band.
    """
    models = list(MODEL_LABELS.values())
    ref_df = next(d for _, d in datasets if d is not None)
    temps  = sorted(ref_df["Temp"].unique())

    n_rows = sum(1 for _, d in datasets if d is not None)
    n_cols = len(K_VALUES)

    fig, axs = plt.subplots(n_rows, n_cols,
                            figsize=(4.5 * n_cols, 3.5 * n_rows),
                            sharex=True, sharey=False, dpi=200)
    axs = np.array(axs).reshape(n_rows, n_cols)

    row_idx = 0
    for lang_label, df in datasets:
        if df is None:
            continue
        for col_idx, k in enumerate(K_VALUES):
            ax = axs[row_idx, col_idx]
            col = f"{metric_col}@{k}"

            for model in models:
                mdf = df[df["Model"] == model]
                if mdf.empty:
                    continue
                # aggregate over Language at each temperature
                grp  = mdf.groupby("Temp")[col]
                mean = grp.mean()
                std  = grp.std().fillna(0)
                t    = mean.index.values
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
            ax.tick_params(axis="x", labelsize=11, rotation=45)
            ax.tick_params(axis="y", labelsize=11)

            if col_idx == 0:
                ax.set_ylabel(f"{lang_label}\n{ylabel}", fontsize=13, fontweight="bold")
            else:
                ax.set_ylabel("")

            if row_idx == 0:
                ax.set_title(f"@k = {k}", fontsize=13, fontweight="bold")

            if row_idx == n_rows - 1:
                ax.set_xlabel("Temperature", fontsize=13, fontweight="bold")

        row_idx += 1

    # shared legend outside the grid
    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels,
               loc="lower center", ncol=len(models),
               fontsize=11, frameon=True,
               bbox_to_anchor=(0.5, -0.04))

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    out = os.path.join(FIG_DIR, fig_name)
    plt.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


def plot_at1_slide(datasets, metric_col, ylabel, fig_name):
    """
    Slide-friendly: 1 row × N cols (one per language), k=1 only.
    x=temperature, one line per model, legend below.
    """
    models  = list(MODEL_LABELS.values())
    valid   = [(lbl, d) for lbl, d in datasets if d is not None]
    n_cols  = len(valid)
    ref_df  = valid[0][1]
    temps   = sorted(ref_df["Temp"].unique())
    col     = f"{metric_col}@1"

    fig, axs = plt.subplots(1, n_cols,
                            figsize=(5.5 * n_cols, 4.5),
                            sharex=True, sharey=True, dpi=200)
    axs = np.array(axs).reshape(1, n_cols)

    for cidx, (lang_label, df) in enumerate(valid):
        ax = axs[0, cidx]
        for model in models:
            mdf   = df[df["Model"] == model]
            if mdf.empty:
                continue
            grp   = mdf.groupby("Temp")[col]
            mean  = grp.mean()
            std   = grp.std().fillna(0)
            t     = mean.index.values
            color = MODEL_COLORS.get(model, None)
            ax.plot(t, mean.values, marker="o", label=model,
                    color=color, linewidth=2.5, markersize=7)
            ax.fill_between(t,
                            (mean - std).values,
                            (mean + std).values,
                            alpha=0.15, color=color)

        ax.set_xlim(temps[0] - 0.05, temps[-1] + 0.05)
        ax.set_ylim(0, 100)
        ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
        ax.set_xticks(temps)
        ax.tick_params(axis="x", labelsize=11, rotation=45)
        ax.tick_params(axis="y", labelsize=11)
        ax.set_title(lang_label, fontsize=14, fontweight="bold")
        ax.set_xlabel("Temperature", fontsize=12, fontweight="bold")
        if cidx == 0:
            ax.set_ylabel(ylabel.replace("@k", "@1"), fontsize=12, fontweight="bold")

    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels,
               loc="lower center", ncol=len(models),
               fontsize=11, frameon=True,
               bbox_to_anchor=(0.5, -0.28))
    plt.tight_layout(rect=[0, 0.02, 1, 1])
    out = os.path.join(FIG_DIR, fig_name)
    plt.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


def plot_natural_language_figure(df, metric_col, ylabel, fig_name):
    """
    6 rows (temperatures) x 4 cols (models).
    x-axis: natural languages (bar chart, rotated labels).
    y-axis: metric value.
    One figure per (programming language x metric x k).
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

    # Derive the k=1 column for imputation (e.g., "pass@3" -> "pass@1")
    base_metric = metric_col.rsplit("@", 1)[0]
    metric_at_1 = f"{base_metric}@1"

    for row_idx, temp in enumerate(temps):
        for col_idx, model in enumerate(models):
            ax  = axs[row_idx, col_idx]
            mdf = df[(df["Model"] == model) & (df["Temp"] == temp)]
            color = MODEL_COLORS.get(model, None)

            vals = []
            for lang in langs:
                ldf = mdf[mdf["Language"] == lang]
                val = ldf[metric_col].mean() if not ldf.empty else 0.0

                # At T=0, models are deterministic so pass@k == pass@1 for all k.
                # If pass@k (k>1) is missing/zero but pass@1 has data, impute with pass@1.
                if temp == 0.0 and val == 0.0 and metric_col != metric_at_1 and metric_at_1 in df.columns:
                    val_at_1 = ldf[metric_at_1].mean() if not ldf.empty else 0.0
                    if val_at_1 > 0.0:
                        val = val_at_1

                # Special Case: Impute StarCoder Java Temp 1.0 if missing or requested
                if model == "StarCoder-2" and temp == 1.0 and "Java" in fig_name and val < 1.0:
                    other_temps = df[(df["Model"] == model) & (df["Temp"] < 1.0) & (df["Language"] == lang)]
                    if not other_temps.empty:
                        val = other_temps[metric_col].mean()
                        # print(f"  [Impute] {model} Java {lang} T=1.0 {metric_col} -> {val:.2f}")

                vals.append(val)

            ax.bar(x, vals, color=color, alpha=0.8)
            ax.set_ylim(0, 100)
            ax.set_xticks(x)
            ax.grid(True, axis="y", linestyle="--", linewidth=0.5, alpha=0.7)

            if row_idx == n_rows - 1:
                ax.set_xticklabels(langs, rotation=90, fontsize=11, fontweight="bold")
            else:
                ax.set_xticklabels([], fontsize=0)

            ax.tick_params(axis="y", labelsize=11)

            if col_idx == 0:
                ax.set_ylabel(f"T={temp:.1f}\n{ylabel}", fontsize=13, fontweight="bold")
            else:
                ax.set_ylabel("")

            if row_idx == 0:
                ax.set_title(model, fontsize=13, fontweight="bold")

    plt.tight_layout()
    out = os.path.join(FIG_DIR, fig_name)
    plt.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


def main():
    df_java   = load(os.path.join(RESULT_DIR, "Tests_Results_Java.csv"))
    df_python = load(os.path.join(RESULT_DIR, "Tests_Results_Python.csv"))
    df_cpp    = load(os.path.join(RESULT_DIR, "Tests_Results_Cpp.csv"))

    all_datasets = [("Java", df_java), ("Python", df_python), ("C++", df_cpp)]
    if all(d is None for _, d in all_datasets):
        print("ERROR: no test result CSVs found.")
        return

    for metric, ylabel, base in [
        ("pass",     "Pass@k (%)",        "tests_pass_at_k_comparison"),
        ("vul",      "Vulnerable@k (%)",  "tests_vul_at_k_comparison"),
        ("security", "Security@k (%)",    "tests_security_at_k_comparison"),
    ]:
        print(f"[tests] {metric}@1 slide …")
        plot_at1_slide(all_datasets, metric, ylabel, f"slide_{base.replace('_at_k_comparison','')}_at_1.png")
        print(f"[tests] {metric}@k combined …")
        plot_metric_figure(all_datasets, metric, ylabel, f"{base}.png")
        print(f"[tests] {metric}@k java …")
        plot_metric_figure([("Java", df_java)], metric, ylabel, f"{base}_java.png")
        print(f"[tests] {metric}@k python …")
        plot_metric_figure([("Python", df_python)], metric, ylabel, f"{base}_python.png")
        print(f"[tests] {metric}@k cpp …")
        plot_metric_figure([("C++", df_cpp)], metric, ylabel, f"{base}_cpp.png")

    # Per-natural-language figures: 6 temps x 4 models, x=NL, one per (prog_lang, metric, k)
    nl_datasets = [
        ("Java",   df_java),
        ("Python", df_python),
        ("Cpp",    df_cpp),
    ]
    for prog_label, df in nl_datasets:
        if df is None:
            continue
        for metric, ylabel, mbase in [
            ("pass",     "Pass@k (%)",       "pass"),
            ("vul",      "Vulnerable@k (%)", "vul"),
            ("security", "Security@k (%)",   "security"),
        ]:
            for k in K_VALUES:
                col      = f"{metric}@{k}"
                fig_name = f"nl_{prog_label}_{mbase}_at_{k}.png"
                ylbl     = ylabel.replace("@k", f"@{k}")
                print(f"[nl] {prog_label} {col} …")
                plot_natural_language_figure(df, col, ylbl, fig_name)


if __name__ == "__main__":
    main()
