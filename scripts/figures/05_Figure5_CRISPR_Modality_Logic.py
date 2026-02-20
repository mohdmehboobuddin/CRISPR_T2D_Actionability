import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "results/tables/Table5_CRISPR_Actionability_Prioritization.tsv"

OUT_DIR = BASE_DIR / "figures/high_dpi"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Figure5_CRISPR_Modality_Logic.png"

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(DATA_FILE, sep="\t")

# Encode modality for plotting
modality_map = {
    "CRISPRi": 1,
    "CRISPR knockout": 2,
    "CRISPRa": 3
}

df["Modality_Code"] = df["CRISPR_Modality"].map(modality_map)

# ----------------------------
# Plot
# ----------------------------
plt.figure(figsize=(8, 5))

colors = {
    "CRISPRi": "#1f77b4",
    "CRISPR knockout": "#d62728",
    "CRISPRa": "#2ca02c"
}

for modality, color in colors.items():
    subset = df[df["CRISPR_Modality"] == modality]
    plt.bar(
        subset["Target_Gene"],
        subset["CRISPR_Actionability_Score"],
        label=modality,
        color=color
    )

plt.ylabel("CRISPR Actionability Score")
plt.xlabel("Target Gene")
plt.title("CRISPR Modality Selection for Prioritized T2D Targets")
plt.legend()

plt.tight_layout()
plt.savefig(OUT_FILE, dpi=400)
plt.close()

print("✅ Figure 5 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
