import pandas as pd

# Load full SNP panel
df = pd.read_csv("results/CRISPR_full_10SNP_panel.tsv", sep="\t")

# ---- Genomic Context Score ----
def genomic_context(row):
    if row["VariantType"] == "Coding":
        return 3
    elif row["EnhancerOverlap"] == 1:
        return 2
    else:
        return 1

# ---- Regulatory Evidence Score ----
def regulatory_score(row):
    if row["EnhancerOverlap"] == 1:
        return 3
    else:
        return 1

# ---- Expression Score ----
def expression_score(tpm):
    if tpm > 10:
        return 2
    elif 1 <= tpm <= 10:
        return 1
    else:
        return 0

# Apply scoring
df["Genomic_Context"] = df.apply(genomic_context, axis=1)
df["Regulatory_Evidence"] = df.apply(regulatory_score, axis=1)
df["Expression_Score"] = df["Expression_TPM"].apply(expression_score)

# Target clarity already provided
df["CAS"] = (
    df["Genomic_Context"] +
    df["Regulatory_Evidence"] +
    df["Expression_Score"] +
    df["Target_Clarity"]
)

# Assign CRISPR modality
df["Modality"] = df["VariantType"].apply(
    lambda x: "CRISPR knockout" if x == "Coding" else "CRISPRi"
)

# Sort by CAS
df = df.sort_values(by="CAS", ascending=False)

# Save final results
df.to_csv("results/CRISPR_actionability_scores.tsv", sep="\t", index=False)

print("CAS scoring complete. File saved as CRISPR_actionability_scores.tsv")
