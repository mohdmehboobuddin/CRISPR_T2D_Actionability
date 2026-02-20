import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE = Path(__file__).resolve().parents[2]

EXPR_FILE = BASE / "data/expression/GSE81608_human_islets_rpkm.txt"
ANNOT_FILE = BASE / "data/expression/GPL6244.annot"
TARGET_FILE = BASE / "results/CRISPR_actionability_scores.tsv"

OUT_DIR = BASE / "results/expression"
OUT_DIR.mkdir(exist_ok=True)

OUT_FILE = OUT_DIR / "CRISPR_targets_islet_expression.tsv"

# -----------------------------
# Load CRISPR targets
# -----------------------------
targets = pd.read_csv(TARGET_FILE, sep="\t")
target_genes = set(targets["Target_Gene"].unique())

print(f"🔍 Loaded {len(target_genes)} CRISPR target genes")

# -----------------------------
# Load annotation (Ensembl → Gene Symbol)
# -----------------------------
annot = pd.read_csv(ANNOT_FILE, sep="\t", comment="#", low_memory=False)

annot = annot[["ENSEMBL_ID", "Gene Symbol"]].dropna()
annot.columns = ["Ensembl_ID", "Gene"]

annot["Ensembl_ID"] = annot["Ensembl_ID"].str.split(".").str[0]

print(f"🧬 Loaded {len(annot)} gene ID mappings")

# -----------------------------
# Load expression matrix
# -----------------------------
expr = pd.read_csv(EXPR_FILE, sep="\t")

# First column is Ensembl ID
expr.rename(columns={expr.columns[0]: "Ensembl_ID"}, inplace=True)
expr["Ensembl_ID"] = expr["Ensembl_ID"].astype(str).str.split(".").str[0]

# -----------------------------
# Merge expression with gene symbols
# -----------------------------
expr = expr.merge(annot, on="Ensembl_ID", how="left")

expr = expr.dropna(subset=["Gene"])

# -----------------------------
# Filter CRISPR target genes
# -----------------------------
expr_targets = expr[expr["Gene"].isin(target_genes)].copy()

if expr_targets.empty:
    raise ValueError("❌ None of the CRISPR target genes found after mapping")

# -----------------------------
# Compute expression statistics
# -----------------------------
sample_cols = [c for c in expr_targets.columns if c.startswith("Sample_")]

expr_targets["Mean_RPKM"] = expr_targets[sample_cols].mean(axis=1)
expr_targets["Median_RPKM"] = expr_targets[sample_cols].median(axis=1)
expr_targets["Max_RPKM"] = expr_targets[sample_cols].max(axis=1)

final = expr_targets[
    ["Gene", "Mean_RPKM", "Median_RPKM", "Max_RPKM"]
].sort_values("Mean_RPKM", ascending=False)

final.to_csv(OUT_FILE, sep="\t", index=False)

print("\n✅ Pancreatic islet expression validation COMPLETE")
print(final)
