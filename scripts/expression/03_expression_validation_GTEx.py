import pandas as pd

# -----------------------------
# Paths
# -----------------------------
GTEX_FILE = "../../data/expression/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct"
TARGET_FILE = "../../results/CRISPR_actionability_scores.tsv"
OUT_FILE = "../../results/expression/CRISPR_targets_GTEx_expression.tsv"

# -----------------------------
# Load CRISPR target genes
# -----------------------------
targets = pd.read_csv(TARGET_FILE, sep="\t")
target_genes = set(targets["Target_Gene"].unique())

print(f"🔍 Loaded {len(target_genes)} CRISPR target genes")

# -----------------------------
# Load GTEx expression
# -----------------------------
expr = pd.read_csv(GTEX_FILE, sep="\t", skiprows=2)

# Keep gene symbol
expr["Gene"] = expr["Description"]

# Keep only target genes
expr_targets = expr[expr["Gene"].isin(target_genes)].copy()

if expr_targets.empty:
    raise ValueError("❌ Target genes not found in GTEx table")

# -----------------------------
# Extract pancreas samples
# -----------------------------
pancreas_cols = [c for c in expr_targets.columns if "Pancreas" in c]

expr_targets["Mean_TPM"] = expr_targets[pancreas_cols].mean(axis=1)
expr_targets["Median_TPM"] = expr_targets[pancreas_cols].median(axis=1)
expr_targets["Max_TPM"] = expr_targets[pancreas_cols].max(axis=1)

final = expr_targets[
    ["Gene", "Mean_TPM", "Median_TPM", "Max_TPM"]
].sort_values("Mean_TPM", ascending=False)

final.to_csv(OUT_FILE, sep="\t", index=False)

print("\n✅ GTEx expression validation COMPLETE")
print(final)
