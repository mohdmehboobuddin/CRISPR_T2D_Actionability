import pandas as pd
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

TABLE5 = BASE_DIR / "results/tables/Table5_CRISPR_Actionability_Prioritization.tsv"
TABLE3 = BASE_DIR / "results/tables/Table3_SNP_TargetGene_CRISPR.tsv"

OUT_DIR = BASE_DIR / "results/tables"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Table6_Final_CRISPR_Targets.tsv"

# ----------------------------
# Load tables
# ----------------------------
t5 = pd.read_csv(TABLE5, sep="\t")
t3 = pd.read_csv(TABLE3, sep="\t")

# ----------------------------
# Merge justification
# ----------------------------
df = t5.merge(
    t3[["SNP", "Functional_Justification"]],
    on="SNP",
    how="left"
)

# ----------------------------
# Rank targets
# ----------------------------
df = df.sort_values(
    by=["CRISPR_Actionability_Score", "Mean_RPKM"],
    ascending=False
).reset_index(drop=True)

df["Rank"] = df.index + 1

# ----------------------------
# Final table
# ----------------------------
final_df = df[[
    "Rank",
    "SNP",
    "Target_Gene",
    "CRISPR_Modality",
    "Islet_Expression_Level",
    "CRISPR_Actionability_Score",
    "Functional_Justification"
]]

# ----------------------------
# Save
# ----------------------------
final_df.to_csv(OUT_FILE, sep="\t", index=False)

print("🏁 FINAL TABLE GENERATED")
print(f"📁 Saved to: {OUT_FILE}")
print("\nPreview:")
print(final_df)
