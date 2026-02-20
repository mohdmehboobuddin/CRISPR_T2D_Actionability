import pandas as pd
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

SCORES_FILE = BASE_DIR / "results/CRISPR_actionability_scores.tsv"
EXPR_FILE = BASE_DIR / "results/tables/Table4_Islet_Expression_Validation.tsv"

OUT_DIR = BASE_DIR / "results/tables"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Table5_CRISPR_Actionability_Prioritization.tsv"

# ----------------------------
# Load data
# ----------------------------
scores = pd.read_csv(SCORES_FILE, sep="\t")
expr = pd.read_csv(EXPR_FILE, sep="\t")

# ----------------------------
# Merge expression support
# ----------------------------
df = scores.merge(
    expr[["Target_Gene", "Mean_RPKM", "Islet_Expression_Level"]],
    on="Target_Gene",
    how="left"
)

# ----------------------------
# Priority classification
# ----------------------------
def priority_class(score):
    if score >= 9:
        return "High Priority"
    elif score >= 7:
        return "Medium Priority"
    else:
        return "Low Priority"

df["Priority_Class"] = df["CRISPR_Actionability_Score"].apply(priority_class)

# ----------------------------
# Final table formatting
# ----------------------------
final_df = df[[
    "SNP",
    "Target_Gene",
    "Tissue",
    "CRISPR_Modality",
    "Mean_RPKM",
    "Islet_Expression_Level",
    "CRISPR_Actionability_Score",
    "Priority_Class"
]].sort_values(
    by="CRISPR_Actionability_Score",
    ascending=False
)

# ----------------------------
# Save
# ----------------------------
final_df.to_csv(OUT_FILE, sep="\t", index=False)

print("✅ Table 5 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
print("\nPreview:")
print(final_df)
