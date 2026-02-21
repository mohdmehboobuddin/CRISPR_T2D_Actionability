import pandas as pd

# Load final CAS file
df = pd.read_csv("results/CRISPR_actionability_scores.tsv", sep="\t")

# -------------------------------
# TABLE 1: GWAS SNP Summary
# -------------------------------
table1 = df[["SNP", "Gene", "VariantType"]].copy()
table1["Disease"] = "Type 2 Diabetes"
table1.to_csv("results/tables/Table1_GWAS_SNP_Summary.tsv", sep="\t", index=False)

# -------------------------------
# TABLE 2: Regulatory Annotation
# -------------------------------
table2 = df[["SNP", "VariantType", "Regulatory_Evidence", "Modality"]].copy()
table2.rename(columns={
    "VariantType": "Variant_Type",
    "Regulatory_Evidence": "Regulatory_Score"
}, inplace=True)
table2.to_csv("results/tables/Table2_Regulatory_Annotation.tsv", sep="\t", index=False)

# -------------------------------
# TABLE 3: SNP to Target Gene
# -------------------------------
table3 = df[["SNP", "Gene", "VariantType", "Pathway", "Modality"]].copy()
table3.rename(columns={
    "Gene": "Target_Gene",
    "VariantType": "Variant_Type"
}, inplace=True)
table3.to_csv("results/tables/Table3_SNP_TargetGene_CRISPR.tsv", sep="\t", index=False)

# -------------------------------
# TABLE 4: Expression Validation
# -------------------------------
table4 = df[["Gene", "Expression_TPM", "Expression_Score"]].copy()
table4.rename(columns={
    "Gene": "Target_Gene",
    "Expression_TPM": "Mean_TPM"
}, inplace=True)
table4 = table4.sort_values(by="Mean_TPM", ascending=False)
table4.to_csv("results/tables/Table4_Islet_Expression_Validation.tsv", sep="\t", index=False)

# -------------------------------
# TABLE 5: CAS Component Breakdown
# -------------------------------
table5 = df[[
    "SNP",
    "Gene",
    "Genomic_Context",
    "Regulatory_Evidence",
    "Expression_Score",
    "Target_Clarity",
    "CAS"
]].copy()
table5.rename(columns={"Gene": "Target_Gene"}, inplace=True)
table5 = table5.sort_values(by="CAS", ascending=False)
table5.to_csv("results/tables/Table5_CRISPR_Actionability_Prioritization.tsv", sep="\t", index=False)

# -------------------------------
# TABLE 6: Final Ranked Targets with Priority Tier
# -------------------------------
table6 = df.copy()

def classify_priority(score):
    if score >= 8:
        return "High Priority"
    elif score >= 6:
        return "Moderate Priority"
    else:
        return "Lower Priority"

table6["Priority_Tier"] = table6["CAS"].apply(classify_priority)

table6 = table6[[
    "SNP",
    "Gene",
    "Genomic_Context",
    "Regulatory_Evidence",
    "Expression_Score",
    "Target_Clarity",
    "CAS",
    "Priority_Tier",
    "Modality",
    "Pathway"
]]

table6 = table6.sort_values(by="CAS", ascending=False)

table6.to_csv("results/tables/Table6_Final_CRISPR_Targets.tsv", sep="\t", index=False)

print("All tables rebuilt successfully from final CAS file.")
