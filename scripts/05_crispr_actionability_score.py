import pandas as pd

# -----------------------------
# CRISPR Actionability Scoring
# -----------------------------

# Final curated SNP → gene mapping
data = [
    ["rs5219",      "KCNJ11",  "Pancreatic islets", "CRISPRi"],
    ["rs10830963",  "MTNR1B",  "Pancreatic islets", "CRISPRi"],
    ["rs7756992",   "CDKAL1",  "Pancreatic islets", "CRISPRi"],
    ["rs13266634",  "SLC30A8", "Pancreatic islets", "CRISPRi"],
    ["rs7172432",   "IRS1",    "Pancreatic islets", "CRISPRi"],
    ["rs12779790",  "TCF7L2",  "Pancreatic islets", "CRISPRi"],
]

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "SNP",
        "Target_Gene",
        "Tissue",
        "CRISPR_Modality"
    ]
)

# -----------------------------
# Scoring framework (locked)
# -----------------------------

df["Noncoding_GWAS"] = 2          # Non-coding GWAS locus
df["Enhancer_Window"] = 3         # ±50 kb enhancer proximity
df["Islet_Specific"] = 3          # Pancreatic islet enhancer
df["Metabolic_Gene"] = 2          # Known metabolic / T2D gene

# Total score
df["CRISPR_Actionability_Score"] = (
    df["Noncoding_GWAS"]
    + df["Enhancer_Window"]
    + df["Islet_Specific"]
    + df["Metabolic_Gene"]
)

# -----------------------------
# Save results (TSV, clean)
# -----------------------------

df.to_csv(
    "../results/CRISPR_actionability_scores.tsv",
    sep="\t",
    index=False,
    header=True
)

# Print to screen for verification
print("\nCRISPR Actionability Score Table:\n")
print(df)
