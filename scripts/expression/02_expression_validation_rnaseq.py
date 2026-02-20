import pandas as pd
import os

# -------------------------------
# Paths
# -------------------------------
RPKM_FILE = "../../data/expression/GSE81608_human_islets_rpkm.txt"
CRISPR_FILE = "../../results/CRISPR_actionability_scores.tsv"
OUT_FILE = "../../results/expression/T2D_expression_validation_rnaseq.tsv"

os.makedirs("../../results/expression", exist_ok=True)

# -------------------------------
# Load CRISPR target genes
# -------------------------------
crispr = pd.read_csv(CRISPR_FILE, sep="\t")
target_genes = crispr["Target_Gene"].unique().tolist()

print(f"🔍 Loaded {len(target_genes)} CRISPR target genes")

# -------------------------------
# Load RNA-seq expression table
# -------------------------------
expr = pd.read_csv(
    RPKM_FILE,
    sep=r"\s+",
    engine="python"
)

# First column is gene symbol
gene_col = expr.columns[0]
expr = expr.rename(columns={gene_col: "Gene"})

# -------------------------------
# Keep only target genes
# -------------------------------
expr = expr[expr["Gene"].isin(target_genes)]

if expr.empty:
    raise ValueError("❌ Target genes not found in RNA-seq table")

# -------------------------------
# Calculate mean expression
# -------------------------------
expr["Mean_Expression"] = expr.iloc[:, 1:].mean(axis=1)

# -------------------------------
# Output
# -------------------------------
out = expr[["Gene", "Mean_Expression"]]
out.to_csv(OUT_FILE, sep="\t", index=False)

print("✅ RNA-seq expression validation complete")
print(f"📄 Saved to: {OUT_FILE}")
