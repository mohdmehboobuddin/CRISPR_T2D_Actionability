import pandas as pd

df = pd.read_csv("results/CRISPR_actionability_scores.tsv", sep="\t")

table6 = df[[
    "SNP",
    "Gene",
    "CAS",
    "Modality",
    "Pathway"
]]

table6 = table6.sort_values(by="CAS", ascending=False)

table6.to_csv("results/tables/Table6_Final_CRISPR_Targets.tsv", sep="\t", index=False)

print("Updated Table 6 generated successfully.")
