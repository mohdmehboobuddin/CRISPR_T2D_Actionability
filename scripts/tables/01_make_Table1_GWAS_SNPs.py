import pandas as pd
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Input files
ALL_SNPS = BASE_DIR / "processed_data/T2D_SNPs.bed"
CODING_SNPS = BASE_DIR / "processed_data/T2D_coding_SNPs.bed"

# Output
OUT_DIR = BASE_DIR / "results/tables"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "Table1_GWAS_SNP_Summary.tsv"

# Load data
cols = ["Chromosome", "Start", "End", "SNP"]
all_df = pd.read_csv(ALL_SNPS, sep="\t", header=None, names=cols)
coding_df = pd.read_csv(CODING_SNPS, sep="\t", header=None, names=cols)

# Classify variant type
coding_set = set(coding_df["SNP"])
all_df["Variant_Type"] = all_df["SNP"].apply(
    lambda snp: "Coding" if snp in coding_set else "Noncoding"
)

# Add metadata
all_df["Position_hg38"] = all_df["Start"] + 1
all_df["Disease"] = "Type 2 Diabetes"

# Final table
final_df = all_df[
    ["SNP", "Chromosome", "Position_hg38", "Variant_Type", "Disease"]
].sort_values("SNP")

# Save
final_df.to_csv(OUT_FILE, sep="\t", index=False)

print("✅ Table 1 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
print(final_df)
