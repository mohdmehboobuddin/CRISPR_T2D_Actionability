import pandas as pd

# Full curated 10 SNP dataset
data = [
    # SNP, Gene, VariantType, EnhancerOverlap(0/1), Expression_TPM, TargetClarity(0-2), Pathway

    ["rs13266634", "SLC30A8", "Coding", 1, 202.30, 2, "Insulin Secretion"],
    ["rs12779790", "TCF7L2", "Non-coding", 1, 12.75, 2, "Beta-cell Regulation"],
    ["rs5219", "KCNJ11", "Coding", 1, 3.85, 2, "Insulin Secretion"],
    ["rs7756992", "CDKAL1", "Non-coding", 1, 9.72, 2, "Insulin Secretion"],
    ["rs7172432", "IRS1", "Non-coding", 0, 0.56, 2, "Insulin Signaling"],
    ["rs10830963", "MTNR1B", "Non-coding", 1, 0.03, 2, "Metabolic Regulation"],

    # Added 4 SNPs
    ["rs1801282", "PPARG", "Coding", 0, 1.20, 2, "Insulin Sensitivity"],
    ["rs4402960", "IGF2BP2", "Non-coding", 1, 5.80, 2, "Beta-cell Function"],
    ["rs7903146", "TCF7L2", "Non-coding", 1, 12.75, 2, "Beta-cell Regulation"],
    ["rs972283", "KLF14", "Non-coding", 0, 0.90, 2, "Metabolic Regulation"],
]

columns = [
    "SNP", "Gene", "VariantType",
    "EnhancerOverlap", "Expression_TPM",
    "Target_Clarity", "Pathway"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("results/CRISPR_full_10SNP_panel.tsv", sep="\t", index=False)

print("Full 10 SNP panel created successfully.")
