import pandas as pd

# -----------------------------
# Paths
# -----------------------------
EXPR_FILE = "../../data/expression/GSE81608_human_islets_rpkm.txt"
TARGET_FILE = "../../results/CRISPR_actionability_scores.tsv"
GTF_FILE = "../../data/annotation/gencode.v44.annotation.gtf"
OUT_FILE = "../../results/expression/CRISPR_targets_islet_expression.tsv"

# -----------------------------
# Load CRISPR target genes
# -----------------------------
targets = pd.read_csv(TARGET_FILE, sep="\t")
target_genes = set(targets["Target_Gene"].unique())

print(f"🔍 Loaded {len(target_genes)} CRISPR target genes")

# -----------------------------
# Build Ensembl → Symbol map
# -----------------------------
gene_map = {}

with open(GTF_FILE) as gtf:
    for line in gtf:
        if line.startswith("#"):
            continue
        fields = line.strip().split("\t")
        if fields[2] != "gene":
            continue

        attrs = fields[8]
        if 'gene_id "' in attrs and 'gene_name "' in attrs:
            gene_id = attrs.split('gene_id "')[1].split('"')[0]
            gene_name = attrs.split('gene_name "')[1].split('"')[0]
            gene_map[gene_id] = gene_name

print(f"🧬 Loaded {len(gene_map)} gene ID mappings")

# -----------------------------
# Load RNA-seq expression
# -----------------------------
expr = pd.read_csv(EXPR_FILE, sep="\t")
expr.rename(columns={expr.columns[0]: "Ensembl_ID"}, inplace=True)

# Remove version numbers (ENSGxxx.1 → ENSGxxx)
expr["Ensembl_ID"] = expr["Ensembl_ID"].str.split(".").str[0]

# Map gene symbols
expr["Gene"] = expr["Ensembl_ID"].map(gene_map)

# Keep only CRISPR targets
expr_targets = expr[expr["Gene"].isin(target_genes)].copy()

if expr_targets.empty:
    raise ValueError("❌ No CRISPR target genes matched after Ensembl mapping")

# -----------------------------
# Convert expression to numeric
# -----------------------------
expr_targets.iloc[:, 1:-1] = expr_targets.iloc[:, 1:-1].apply(
    pd.to_numeric, errors="coerce"
)

# -----------------------------
# Compute stats
# -----------------------------
expr_targets["Mean_RPKM"] = expr_targets.iloc[:, 1:-1].mean(axis=1)
expr_targets["Median_RPKM"] = expr_targets.iloc[:, 1:-1].median(axis=1)
expr_targets["Max_RPKM"] = expr_targets.iloc[:, 1:-1].max(axis=1)

# -----------------------------
# Final table
# -----------------------------
final = expr_targets[
    ["Gene", "Mean_RPKM", "Median_RPKM", "Max_RPKM"]
].sort_values("Mean_RPKM", ascending=False)

final.to_csv(OUT_FILE, sep="\t", index=False)

print("\n✅ Expression validation SUCCESSFUL")
print(f"📁 Saved to: {OUT_FILE}")
print("\n📊 Final results:")
print(final)
