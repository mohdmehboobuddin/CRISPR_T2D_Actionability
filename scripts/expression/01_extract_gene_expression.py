import pandas as pd

# Path to GEO series matrix
file_path = "../../data/expression/GSE38642_series_matrix.txt"

# Read expression data (skip metadata lines starting with '!')
expr = pd.read_csv(
    file_path,
    sep="\t",
    comment="!",
    index_col=0
)

# CRISPR-prioritized genes
genes_of_interest = [
    "KCNJ11",
    "MTNR1B",
    "CDKAL1",
    "SLC30A8",
    "IRS1",
    "TCF7L2"
]

# Subset expression matrix
expr_subset = expr.loc[expr.index.intersection(genes_of_interest)]

# Save extracted data
output_file = "../../results/expression/T2D_gene_expression_raw.tsv"
expr_subset.to_csv(output_file, sep="\t")

print("✅ Extracted expression for genes:")
for g in expr_subset.index:
    print(" -", g)

print("\nSaved to:", output_file)
