import pandas as pd
import numpy as np

# -----------------------------
# Paths
# -----------------------------
EXPR_FILE = "../../data/expression/GSE81608_human_islets_rpkm.txt"
TARGET_FILE = "../../results/CRISPR_actionability_scores.tsv"
OUT_FILE = "../../results/expression/CRISPR_targets_islet_expression.tsv"

# -----------------------------
# Load CRISPR target genes
# -----------------------------
targets = pd.read_csv(TARGET_FILE, sep="\t")
target_genes = sorted(targets["Target_Gene"].unique().tolist())

print(f"🔍 Loaded {len(target_genes)} CRISPR target genes")

# -----------------------------
# Load RNA-seq expression
# -----------------------------
expr = pd.read_csv(EXPR_FILE, sep="\t")

# Normalize gene column name
gene_col = expr.columns[0]
expr.rename(columns={gene_col: "Gene"}, inplace=True)

# Ensure numeric values
expr.iloc[:, 1:] = expr.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

# -----------------------------
# Subset target genes
# -----------------------------
expr_targets = expr[expr["Gene"].isin(target_genes)].copy()

if expr_targets.empty:
    raise ValueError("❌ None of the CRISPR target genes found in RNA-seq table")

# -----------------------------
# Compute statistics
# -----------------------------
expr_targets["Mean_RPKM"] = expr_targets.iloc[:, 1:].mean(axis=1)
expr_targets["Median_RPKM"] = expr_targets.iloc[:, 1:].median(axis=1)
expr_targets["Max_RPKM"] = expr_targets.iloc[:, 1:].max(axis=1)

# -----------------------------
# Final table
# -----------------------------
final = expr_targets[["Gene", "Mean_RPKM", "Median_RPKM", "Max_RPKM"]] \
    .sort_values("Mean_RPKM", ascending=False)

final.to_csv(OUT_FILE, sep="\t", index=False)

print("\n✅ Expression validation complete")
print(f"📁 Saved to: {OUT_FILE}")
print("\n📊 Summary:")
print(final)
