import pandas as pd
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

TABLE1 = BASE_DIR / "results/tables/Table1_GWAS_SNP_Summary.tsv"
OUT_DIR = BASE_DIR / "results/tables"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Table2_Regulatory_Annotation.tsv"

# ----------------------------
# Load GWAS SNP table
# ----------------------------
df = pd.read_csv(TABLE1, sep="\t")

# ----------------------------
# Assign regulatory annotations
# ----------------------------
df["Regulatory_Evidence"] = df["Variant_Type"].apply(
    lambda x: "GWAS noncoding regulatory variant" if x == "Noncoding" else "Protein-coding variant"
)

df["Tissue_Context"] = "Pancreatic islets"

df["CRISPR_Relevance"] = df["Variant_Type"].apply(
    lambda x: "CRISPRi / CRISPRa (regulatory modulation)" if x == "Noncoding" else "CRISPR knockout (gene disruption)"
)

# ----------------------------
# Final table (NO Target_Gene here)
# ----------------------------
final_df = df[[
    "SNP",
    "Variant_Type",
    "Regulatory_Evidence",
    "Tissue_Context",
    "CRISPR_Relevance"
]]

final_df.to_csv(OUT_FILE, sep="\t", index=False)

print("✅ Table 2 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
print("\nPreview:")
print(final_df.head())
