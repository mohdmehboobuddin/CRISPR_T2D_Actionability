import pandas as pd
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

EXPR_FILE = BASE_DIR / "results/expression/CRISPR_islet_expression_validation.tsv"

OUT_DIR = BASE_DIR / "results/tables"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Table4_Islet_Expression_Validation.tsv"

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(EXPR_FILE, sep="\t")

print("📊 Columns found:", list(df.columns))

# ----------------------------
# Required columns
# ----------------------------
required_cols = ["Target_Gene", "Mean_RPKM", "Expression_Rank"]

missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"❌ Missing required columns: {missing}")

# ----------------------------
# Derive expression category
# ----------------------------
def classify_expression(rpkm):
    if rpkm >= 10:
        return "High"
    elif rpkm >= 1:
        return "Moderate"
    else:
        return "Low"

df["Islet_Expression_Level"] = df["Mean_RPKM"].apply(classify_expression)

df["Expression_Evidence"] = df["Islet_Expression_Level"].map(
    {
        "High": "Strong pancreatic islet expression",
        "Moderate": "Moderate pancreatic islet expression",
        "Low": "Low or negligible expression in islets",
    }
)

# ----------------------------
# Final Table 4
# ----------------------------
final_df = df[
    [
        "Target_Gene",
        "Mean_RPKM",
        "Expression_Rank",
        "Islet_Expression_Level",
        "Expression_Evidence",
    ]
].sort_values("Expression_Rank")

# ----------------------------
# Save
# ----------------------------
final_df.to_csv(OUT_FILE, sep="\t", index=False)

print("✅ Table 4 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
print("\nPreview:")
print(final_df.head())

