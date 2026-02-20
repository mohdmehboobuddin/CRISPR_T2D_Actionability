import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "results/tables/Table5_CRISPR_Actionability_Prioritization.tsv"

OUT_DIR = BASE_DIR / "figures/high_dpi"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Figure7_CRISPR_Prioritization_Heatmap.png"

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(DATA_FILE, sep="\t")
print("📊 Columns found:", list(df.columns))

# ----------------------------
# Encode categorical biology → numeric
# ----------------------------
expression_map = {
    "Low": 1,
    "Moderate": 2,
    "Strong": 3
}

modality_map = {
    "CRISPRi": 2,
    "CRISPRa": 2,
    "CRISPR knockout": 3
}

df["Islet_Expression_Score"] = df["Islet_Expression_Level"].map(expression_map)
df["CRISPR_Modality_Score"] = df["CRISPR_Modality"].map(modality_map)

# ----------------------------
# Build heatmap table
# ----------------------------
heatmap_df = df.set_index("Target_Gene")[[
    "Islet_Expression_Score",
    "CRISPR_Modality_Score",
    "CRISPR_Actionability_Score"
]]

# ----------------------------
# Plot heatmap
# ----------------------------
plt.figure(figsize=(8, 4.5))

sns.heatmap(
    heatmap_df,
    annot=True,
    cmap="YlOrRd",
    linewidths=0.6,
    cbar_kws={"label": "Evidence Strength"},
    fmt=".0f"
)

plt.title("Integrated CRISPR Target Prioritization for Type 2 Diabetes")
plt.ylabel("Target Gene")
plt.xlabel("Evidence Layer")

plt.tight_layout()
plt.savefig(OUT_FILE, dpi=400)
plt.close()

print("✅ Figure 7 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
