"""
Four separate figures for language-family table insights.
"""

import numpy as np
import matplotlib.pyplot as plt

DATA = {
    "Afro-Asiatic": {
        "GPT-4o": [15.99,29.77,34.39, 25.60,42.33,36.09, 17.57,33.23,37.78, 22.04,38.20,31.61, 18.37,34.27,39.11, 20.77,37.27,30.23],
        "Gemini":  [12.58,17.28,31.26, 14.92,36.40,23.76, 17.07,24.27,37.67, 10.08,21.80,17.01, 19.22,27.08,39.54,  8.27,16.13,14.60],
        "Qwen":    [ 8.35,16.84, 7.59, 20.63,32.27,11.91, 13.57,21.49,15.43, 12.43,13.40, 2.82, 16.02,24.84,20.16,  9.34, 8.73, 1.86],
        "SC2":     [ 0.36, 0.74, 1.22,  1.01, 6.13, 1.65,  1.05, 1.53, 2.67,  0.00, 0.27, 0.00,  1.69, 2.41, 3.99,  0.00, 0.13, 0.00],
    },
    "Austro-Asiatic": {
        "GPT-4o": [15.30,28.48,35.94, 26.88,45.47,34.30, 17.53,32.38,39.67, 23.52,42.27,30.17, 18.56,33.66,41.07, 22.18,41.33,29.20],
        "Gemini":  [13.05,16.93,30.49, 16.53,38.13,25.21, 17.55,23.57,38.15, 11.42,25.60,18.32, 19.36,26.10,40.04,  9.81,20.80,15.15],
        "Qwen":    [ 8.08,16.55, 7.92, 20.03,29.33,10.19, 12.67,21.06,15.93, 11.42,10.40, 2.62, 15.17,24.74,20.34,  7.93, 6.40, 1.52],
        "SC2":     [ 0.89, 0.81, 0.81,  0.94, 7.47, 0.83,  2.01, 2.28, 2.23,  0.00, 0.00, 0.00,  3.01, 3.58, 3.45,  0.00, 0.00, 0.00],
    },
    "Austronesian": {
        "GPT-4o": [17.42,29.52,35.63, 24.69,44.89,35.49, 19.50,32.94,39.03, 21.42,40.58,30.62, 20.31,33.95,40.22, 20.12,38.89,29.25],
        "Gemini":  [11.82,16.51,31.07, 14.52,37.51,24.79, 15.63,23.14,37.56,  9.36,22.31,16.90, 17.49,25.68,39.38,  8.33,17.69,14.55],
        "Qwen":    [ 9.13,16.66, 7.19, 19.35,27.24,10.79, 14.59,21.07,15.05, 11.20, 9.87, 2.57, 17.45,24.48,19.77,  8.56, 6.58, 1.70],
        "SC2":     [ 0.50, 0.68, 0.63,  0.49, 6.53, 0.73,  1.10, 1.74, 1.77,  0.00, 0.27, 0.00,  1.72, 2.73, 2.78,  0.00, 0.09, 0.00],
    },
    "I-E (Germanic)": {
        "GPT-4o": [16.66,30.37,35.96, 24.05,43.57,34.33, 18.38,33.43,39.26, 20.80,39.57,30.17, 19.03,34.36,40.39, 19.45,37.77,28.79],
        "Gemini":  [12.07,17.54,32.80, 13.05,37.87,23.52, 16.25,23.94,39.26,  8.45,24.03,16.12, 18.18,26.51,41.00,  7.08,19.27,13.40],
        "Qwen":    [ 8.93,16.75, 8.25, 17.58,27.10,10.33, 14.46,21.93,16.64, 10.23, 9.70, 2.00, 17.38,25.56,21.40,  7.61, 6.73, 1.10],
        "SC2":     [ 0.81, 0.81, 0.58,  0.94, 7.83, 0.52,  1.60, 1.87, 1.62,  0.00, 0.27, 0.00,  2.44, 2.93, 2.51,  0.00, 0.03, 0.00],
    },
    "I-E (Greek)": {
        "GPT-4o": [15.74,29.37,34.33, 23.39,41.73,34.44, 17.56,32.36,37.20, 18.95,37.20,31.13, 18.34,33.49,38.34, 17.47,35.87,29.89],
        "Gemini":  [12.35,15.02,31.59, 15.32,34.53,25.07, 17.01,20.04,37.18,  9.95,22.93,18.18, 18.84,22.30,38.60,  8.20,18.13,15.56],
        "Qwen":    [ 7.97,14.49, 7.88, 16.94,28.13,11.98, 13.90,18.27,15.57,  8.87, 9.33, 3.03, 16.91,21.71,19.93,  6.99, 6.93, 2.07],
        "SC2":     [ 0.52, 1.32, 0.83,  0.67, 6.80, 0.96,  1.09, 2.80, 2.32,  0.00, 0.13, 0.00,  1.70, 4.26, 3.64,  0.00, 0.00, 0.00],
    },
    "I-E (Iranian)": {
        "GPT-4o": [16.90,28.31,35.70, 23.66,40.27,33.20, 17.87,31.70,38.83, 21.64,36.40,29.61, 18.19,32.54,40.00, 20.70,35.07,28.93],
        "Gemini":  [14.05,17.33,30.48, 14.92,36.00,23.97, 19.29,23.66,37.32,  9.68,22.27,15.29, 21.53,26.05,39.03,  7.66,17.87,12.40],
        "Qwen":    [ 7.03,17.09, 7.56, 15.32,30.27,10.47, 11.67,20.82,15.32,  8.87,10.67, 2.62, 14.05,24.03,19.83,  6.45, 7.33, 1.93],
        "SC2":     [ 0.15, 1.28, 1.34,  0.40, 7.07, 0.83,  0.43, 2.19, 3.18,  0.00, 0.13, 0.14,  0.71, 3.22, 4.75,  0.00, 0.13, 0.14],
    },
    "I-E (Romance)": {
        "GPT-4o": [16.87,30.10,35.26, 23.82,44.37,35.16, 18.51,33.09,38.70, 20.19,40.13,30.96, 19.15,33.96,39.91, 18.99,38.63,29.72],
        "Gemini":  [12.15,15.18,31.69, 14.65,36.47,24.21, 16.07,21.47,38.27, 10.28,23.83,17.42, 17.93,24.06,40.04,  8.57,19.20,14.50],
        "Qwen":    [ 8.75,17.65, 8.45, 19.42,29.70,10.30, 14.21,22.62,16.73, 11.73,11.07, 2.62, 16.98,26.40,21.30,  9.14, 7.10, 1.58],
        "SC2":     [ 0.83, 0.86, 0.67,  0.77, 7.27, 1.03,  1.57, 2.26, 1.88,  0.00, 0.27, 0.03,  2.36, 3.57, 2.92,  0.00, 0.10, 0.00],
    },
    "Sino-Tibetan": {
        "GPT-4o": [16.26,33.85,36.25, 25.67,42.80,36.91, 18.61,36.37,39.87, 20.56,39.07,32.92, 19.64,36.98,41.08, 19.09,37.33,31.68],
        "Gemini":  [10.57,15.48,30.10, 14.78,36.53,23.14, 14.38,22.73,37.28,  8.33,22.80,14.05, 16.18,25.32,39.68,  7.12,17.20,11.16],
        "Qwen":    [ 9.73,21.43, 6.94, 18.82,25.73, 9.78, 14.89,25.89,14.38, 10.22, 8.53, 2.20, 17.55,29.55,18.78,  8.06, 6.13, 1.38],
        "SC2":     [ 0.27, 0.83, 0.55,  0.81, 6.13, 0.41,  0.80, 1.80, 1.60,  0.00, 0.27, 0.00,  1.31, 2.77, 2.57,  0.00, 0.00, 0.00],
    },
    "Slavic": {
        "GPT-4o": [15.36,29.54,34.69, 23.12,40.13,33.68, 17.14,32.68,38.12, 18.88,36.33,29.41, 17.77,33.77,39.36, 17.27,35.00,28.24],
        "Gemini":  [11.45,16.18,29.77, 13.98,36.53,25.21, 15.99,22.60,36.50,  9.74,23.67,17.56, 18.30,24.99,38.28,  8.13,18.00,13.98],
        "Qwen":    [ 8.37,17.93, 7.86, 19.96,29.13,10.81, 14.25,22.98,15.27, 11.96,10.40, 2.13, 17.34,26.59,19.44,  8.94, 7.33, 1.52],
        "SC2":     [ 0.60, 1.27, 0.83,  0.87, 7.73, 0.62,  1.48, 2.56, 2.08,  0.00, 0.60, 0.00,  2.33, 3.92, 3.16,  0.00, 0.13, 0.00],
    },
    "Turkic": {
        "GPT-4o": [18.28,28.51,33.84, 23.25,42.27,36.91, 20.41,31.28,36.63, 20.30,39.33,32.92, 21.26,31.89,37.50, 19.22,38.53,31.54],
        "Gemini":  [13.90,16.43,30.10, 16.53,35.87,26.72, 17.93,22.39,36.98, 11.96,20.13,15.98, 19.81,24.80,39.13, 10.08,14.27,12.81],
        "Qwen":    [ 7.42,17.29, 7.13, 17.61,28.40,13.36, 12.60,21.32,14.57,  8.87, 9.60, 2.48, 15.53,25.00,18.83,  7.39, 5.87, 1.38],
        "SC2":     [ 0.83, 0.63, 0.72,  0.94, 7.87, 1.10,  1.93, 1.75, 2.07,  0.00, 0.00, 0.00,  3.00, 2.73, 3.32,  0.00, 0.00, 0.00],
    },
    "Uralic": {
        "GPT-4o": [16.44,28.12,33.37, 23.57,42.89,36.13, 18.82,31.50,36.41, 20.16,39.20,31.86, 19.74,32.57,37.53, 19.00,37.47,30.30],
        "Gemini":  [11.82,16.93,31.11, 14.02,35.42,24.66, 16.18,22.82,37.74,  9.45,21.38,17.03, 18.26,25.02,39.72,  8.06,15.96,13.64],
        "Qwen":    [ 7.43,14.56, 7.75, 19.00,25.64,11.11, 12.72,18.73,15.22,  9.45, 8.93, 2.30, 15.57,22.13,19.43,  7.30, 5.56, 1.29],
        "SC2":     [ 0.46, 0.76, 0.97,  1.30, 6.67, 0.83,  1.13, 1.88, 2.16,  0.04, 0.36, 0.00,  1.75, 2.86, 3.30,  0.00, 0.09, 0.00],
    },
}

# Index layout per row:
# 0-2:  Pass@1 J,P,C  |  3-5:  Sec@1 J,P,C
# 6-8:  Pass@3 J,P,C  |  9-11: Sec@3 J,P,C
# 12-14:Pass@5 J,P,C  | 15-17: Sec@5 J,P,C
P1J,P1P,P1C = 0,1,2
S1J,S1P,S1C = 3,4,5
P3J,P3P,P3C = 6,7,8
S3J,S3P,S3C = 9,10,11
P5J,P5P,P5C = 12,13,14
S5J,S5P,S5C = 15,16,17

FAMILIES = list(DATA.keys())
MODELS   = ["GPT-4o", "Gemini", "Qwen", "SC2"]

arr = np.array([[DATA[f][m] for m in MODELS] for f in FAMILIES])  # (11,4,18)
grand_avg = arr.mean(axis=(0, 1))

pass_J = [grand_avg[P1J], grand_avg[P3J], grand_avg[P5J]]
pass_P = [grand_avg[P1P], grand_avg[P3P], grand_avg[P5P]]
pass_C = [grand_avg[P1C], grand_avg[P3C], grand_avg[P5C]]
sec_J  = [grand_avg[S1J], grand_avg[S3J], grand_avg[S5J]]
sec_P  = [grand_avg[S1P], grand_avg[S3P], grand_avg[S5P]]
sec_C  = [grand_avg[S1C], grand_avg[S3C], grand_avg[S5C]]

LC = {"Java": "#E07B54", "Python": "#5B9BD5", "C++": "#70AD47"}
MC = {"GPT-4o": "#2C7BB6", "Gemini": "#D7191C", "Qwen": "#FDAE61", "SC2": "#ABDDA4"}

SAVE_DIR = "Result_Generation/Figure"

# ──────────────────────────────────────────────────────────────────
# Figure 1 — Java is harder on both axes
# ──────────────────────────────────────────────────────────────────
fig1, ax = plt.subplots(figsize=(7, 5))
x, w = np.arange(3), 0.22
for i, (lang, pv, sv) in enumerate(
        [("Java", pass_J, sec_J), ("Python", pass_P, sec_P), ("C++", pass_C, sec_C)]):
    off = (i - 1) * w
    ax.bar(x + off - 0.12, pv, w, color=LC[lang], label=lang, alpha=0.85, edgecolor="white")
    ax.bar(x + off + 0.12, sv, w, color=LC[lang], alpha=0.45, edgecolor="white", hatch="//")
ax.set_xticks(x)
ax.set_xticklabels(["k = 1", "k = 3", "k = 5"])
ax.set_ylabel("Score (%)")
ax.set_ylim(0, 50)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
ax.set_axisbelow(True)
# legend: language patches + dummy patches for Pass/Security
from matplotlib.patches import Patch
handles = [Patch(facecolor=LC[l], label=l) for l in ["Java", "Python", "C++"]]
handles += [Patch(facecolor="grey", alpha=0.85, label="Pass@k"),
            Patch(facecolor="grey", alpha=0.45, hatch="//", label="Security@k")]
ax.legend(handles=handles, fontsize=8, loc="upper left")
fig1.tight_layout()
fig1.savefig(f"{SAVE_DIR}/lf_java_harder.png", dpi=150, bbox_inches="tight")
print("Saved lf_java_harder.png")
plt.close(fig1)

# ──────────────────────────────────────────────────────────────────
# Figure 2 — Consistent language trend (grouped bar per metric)
# ──────────────────────────────────────────────────────────────────
fig2, ax = plt.subplots(figsize=(8, 5))
metrics = ["Pass@1", "Sec@1", "Pass@3", "Sec@3", "Pass@5", "Sec@5"]
idxs    = [(P1J,P1P,P1C),(S1J,S1P,S1C),(P3J,P3P,P3C),(S3J,S3P,S3C),(P5J,P5P,P5C),(S5J,S5P,S5C)]
xpos, w = np.arange(len(metrics)), 0.25
for i, (lang, col) in enumerate([("Java","#E07B54"),("Python","#5B9BD5"),("C++","#70AD47")]):
    vals = [grand_avg[idxs[m][i]] for m in range(6)]
    ax.bar(xpos + (i-1)*w, vals, w, color=col, label=lang, alpha=0.85, edgecolor="white")
ax.set_xticks(xpos)
ax.set_xticklabels(metrics, rotation=30, ha="right", fontsize=9)
ax.set_ylabel("Score (%)")
ax.set_ylim(0, 50)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
ax.set_axisbelow(True)
ax.legend(fontsize=9)
fig2.tight_layout()
fig2.savefig(f"{SAVE_DIR}/lf_language_trend.png", dpi=150, bbox_inches="tight")
print("Saved lf_language_trend.png")
plt.close(fig2)

# ──────────────────────────────────────────────────────────────────
# Figure 3 — Scaling with k (line chart)
# ──────────────────────────────────────────────────────────────────
fig3, ax = plt.subplots(figsize=(7, 5))
k_vals = [1, 3, 5]
for lang, pv, sv, col in [
        ("Java",   pass_J, sec_J, "#E07B54"),
        ("Python", pass_P, sec_P, "#5B9BD5"),
        ("C++",    pass_C, sec_C, "#70AD47")]:
    ax.plot(k_vals, pv, color=col, linestyle="-",  marker="o", linewidth=2.2,
            markersize=7, label=f"{lang} — Pass@k")
    ax.plot(k_vals, sv, color=col, linestyle="--", marker="s", linewidth=2.2,
            markersize=7, label=f"{lang} — Security@k")
ax.set_xticks(k_vals)
ax.set_xlabel("k", fontsize=11)
ax.set_ylabel("Score (%)", fontsize=11)
ax.set_ylim(0, 45)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
ax.set_axisbelow(True)
ax.legend(fontsize=8, ncol=2)
fig3.tight_layout()
fig3.savefig(f"{SAVE_DIR}/lf_scaling_k.png", dpi=150, bbox_inches="tight")
print("Saved lf_scaling_k.png")
plt.close(fig3)

# ──────────────────────────────────────────────────────────────────
# Figure 4 — Model ranking stability (line per model across families)
# ──────────────────────────────────────────────────────────────────
fig4, ax = plt.subplots(figsize=(9, 5))
fam_model_pass5 = np.array([
    [arr[fi, mi, P5J:P5C+1].mean() for mi in range(4)]
    for fi in range(len(FAMILIES))
])
x_fam = np.arange(len(FAMILIES))
short_fam = [f.replace("I-E (", "IE-").replace(")", "") for f in FAMILIES]
for mi, model in enumerate(MODELS):
    ax.plot(x_fam, fam_model_pass5[:, mi], color=list(MC.values())[mi],
            marker="o", linewidth=2.2, markersize=6, label=model)
ax.set_xticks(x_fam)
ax.set_xticklabels(short_fam, rotation=35, ha="right", fontsize=8)
ax.set_ylabel("Avg Pass@5 (%)", fontsize=11)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
ax.set_axisbelow(True)
ax.legend(fontsize=9)
fig4.tight_layout()
fig4.savefig(f"{SAVE_DIR}/lf_model_stability.png", dpi=150, bbox_inches="tight")
print("Saved lf_model_stability.png")
plt.close(fig4)
