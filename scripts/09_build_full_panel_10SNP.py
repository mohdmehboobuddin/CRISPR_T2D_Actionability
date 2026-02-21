import pandas as pd

data = [
    # SNP, Gene, VariantType, EnhancerOverlap (0/1), Expression_TPM, Pathway

    ["rs13266634", "SLC30A8", "Coding", 1, 202.3, "Insulin Secretion"],
    ["rs12779790", "TCF7L2", "Non-coding", 1, 12.75, "Beta-cell Regulation"],
    ["rs5219", "KCNJ11", "Coding", 1, 3.85, "Insulin Secretion"],
    ["rs7756992", "CDKAL1", "Non-coding", 1, 9.72, "Insulin Secretion"],
    ["rs7172432", "IRS1", "Non-coding", 0, 0.56, "Insulin Signaling"],
    ["rs10830963", "MTNR1B", "Non-coding", 1, 0.03, "Metabolic Regulation"],

    # Newly added 4 SNPs
    ["rs1801282", "PPARG", "Coding", 0, 1.2, "Insulin Sensitivity"],
    ["rs4402960", "IGF2BP2", "Non-coding", 1, 5.8, "Beta-cell Function"],
    ["rs7903146", "TCF7L2", "Non-coding", 1, 12.75, "Beta-cell Regulation"],
    ["rs972283", "KLF14", "Non-coding", 0, 0.9, "Metabolic Regulation"],
]

df = pd.DataFrame(data, columns=[
    "SNP", "Gene", "VariantType",
    "EnhancerOverlap", "Expression_TPM", "Pathway"
])

df.to_csv("results/CRISPR_full_10SNP_panel.tsv", sep="\t", index=False)

print("Full 10 SNP panel saved.")
