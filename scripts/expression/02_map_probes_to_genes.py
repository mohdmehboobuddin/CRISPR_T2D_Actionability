import GEOparse
import pandas as pd

# ===============================
# SETTINGS
# ===============================
GSE_ID = "GSE38642"
OUT_FILE = "../../results/expression/T2D_gene_expression_genelevel.tsv"

GENES = [
    "KCNJ11",
    "MTNR1B",
    "CDKAL1",
    "SLC30A8",
    "IRS1",
    "TCF7L2"
]

# ===============================
# LOAD GEO DATASET
# ===============================
gse = GEOparse.get_GEO(geo=GSE_ID, destdir="../../data/expression")

# Get expression matrix
expr = gse.pivot_samples("VALUE")

# ===============================
# GET PROBE → GENE MAPPING
# ===============================
gpl = list(gse.gpls.values())[0]
annot = gpl.table

# Try common gene symbol columns
gene_col = None
for col in annot.columns:
    if "Gene Symbol" in col or col.lower() == "symbol":
        gene_col = col
        break

if gene_col is None:
    raise ValueError("❌ Gene symbol column not found in GPL table")

annot = annot[[annot.columns[0], gene_col]]
annot.columns = ["ProbeID", "Gene"]

# ===============================
# MERGE EXPRESSION + ANNOTATION
# ===============================
expr["ProbeID"] = expr.index
merged = expr.merge(annot, on="ProbeID", how="left")

# ===============================
# FILTER TARGET GENES
# ===============================
filtered = merged[merged["Gene"].isin(GENES)]

if filtered.empty:
    raise ValueError("❌ No target genes found after mapping")

# ===============================
# COLLAPSE PROBES → GENE LEVEL
# ===============================
gene_expr = (
    filtered
    .drop(columns=["ProbeID"])
    .groupby("Gene")
    .mean()
)

# ===============================
# SAVE OUTPUT
# ===============================
gene_expr.to_csv(OUT_FILE, sep="\t")

# ===============================
# REPORT
# ===============================
print("\n✅ SUCCESS — Gene-level expression extracted using GEOparse")
print("Genes:")
for g in gene_expr.index:
    print(" -", g)

print("\nSaved to:", OUT_FILE)

