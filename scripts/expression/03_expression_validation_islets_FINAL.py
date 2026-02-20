import pandas as pd

# -----------------------------
# File paths
# -----------------------------
CRISPR_FILE = "../../results/CRISPR_actionability_scores.tsv"
EXPR_FILE = "../../data/expression/GSE81608_human_islets_rpkm.txt"
MAP_FILE = "../../data/expression/gene_symbol_to_entrez.tsv"
OUT_FILE = "../../results/expression/CRISPR_islet_expression_validation.tsv"

# -----------------------------
# Load CRISPR genes
# -----------------------------
crispr = pd.read_csv(CRISPR_FILE, sep="\t")
target_genes = crispr["Target_Gene"].unique()

print(f"🔍 Loaded {len(target_genes)} CRISPR target genes")

# -----------------------------
# Load gene mapping
# -----------------------------
mapping = pd.read_csv(MAP_FILE, sep="\t")
mapping["Entrez_ID"] = mapping["Entrez_ID"].astype(str)

# -----------------------------
# Load RNA-seq data
# -----------------------------
expr = pd.read_csv(EXPR_FILE, sep="\t")
expr.rename(columns={expr.columns[0]: "Entrez_ID"}, inplace=True)
expr["Entrez_ID"] = expr["Entrez_ID"].astype(str)

# Convert expression values to numeric
expr.iloc[:, 1:] = expr.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")
expr["Mean_RPKM"] = expr.iloc[:, 1:].mean(axis=1)

# -----------------------------
# Merge expression with mapping
# -----------------------------
merged = pd.merge(mapping, expr, on="Entrez_ID", how="inner")

if merged.empty:
    raise ValueError("❌ No CRISPR target genes found after Entrez mapping")

# -----------------------------
# Rank expression
# -----------------------------
merged["Expression_Rank"] = merged["Mean_RPKM"].rank(
    ascending=False, method="min"
)

out = merged[
    ["Target_Gene", "Entrez_ID", "Mean_RPKM", "Expression_Rank"]
].sort_values("Mean_RPKM", ascending=False)

out.to_csv(OUT_FILE, sep="\t", index=False)

print("✅ Expression validation SUCCESSFUL")
print(f"📁 Saved to: {OUT_FILE}")
