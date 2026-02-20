import pandas as pd
import os

# -------------------------------
# Paths
# -------------------------------
MATRIX_FILE = "../../data/expression/GSE38642_series_matrix.txt"
CRISPR_FILE = "../../results/CRISPR_actionability_scores.tsv"
OUT_FILE = "../../results/expression/T2D_expression_validation_matrix.tsv"

os.makedirs("../../results/expression", exist_ok=True)

# -------------------------------
# Load CRISPR target genes
# -------------------------------
crispr = pd.read_csv(CRISPR_FILE, sep="\t")
target_genes = crispr["Target_Gene"].unique().tolist()

print(f"🔍 Loaded {len(target_genes)} CRISPR target genes")

# -------------------------------
# Load expression matrix
# -------------------------------
expr = pd.read_csv(
    MATRIX_FILE,
    sep="\t",
    comment="!",
    index_col=0
)

print(f"📊 Expression matrix shape: {expr.shape}")

# -------------------------------
# Keep only target genes
# -------------------------------
expr = expr.loc[expr.index.intersection(target_genes)]

if expr.empty:
    raise ValueError("❌ None of the target genes found in expression matrix")

# -------------------------------
# Calculate mean expression
# -------------------------------
expr["Mean_Expression"] = expr.mean(axis=1)

# -------------------------------
# Prepare output
# -------------------------------
out = expr[["Mean_Expression"]].reset_index()
out.columns = ["Gene", "Mean_Expression"]

out.to_csv(OUT_FILE, sep="\t", index=False)

print("✅ Expression validation (microarray) complete")
print(f"📄 Saved to: {OUT_FILE}")
