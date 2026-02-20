import pandas as pd
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
OUT_DIR = BASE_DIR / "results/tables"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Table3_SNP_TargetGene_CRISPR.tsv"

# ----------------------------
# SNP → Target gene mapping
# ----------------------------
data = [
    {
        "SNP": "rs5219",
        "Target_Gene": "KCNJ11",
        "Mapping_Rationale": "Coding variant affecting potassium channel",
        "Tissue": "Pancreatic islets",
        "CRISPR_Modality": "CRISPR knockout",
        "Functional_Justification": "Loss-of-function modeling of coding mutation"
    },
    {
        "SNP": "rs10830963",
        "Target_Gene": "MTNR1B",
        "Mapping_Rationale": "Islet-specific eQTL",
        "Tissue": "Pancreatic islets",
        "CRISPR_Modality": "CRISPRi",
        "Functional_Justification": "Regulatory repression of overexpressed risk gene"
    },
    {
        "SNP": "rs7756992",
        "Target_Gene": "CDKAL1",
        "Mapping_Rationale": "Islet eQTL linked to insulin secretion",
        "Tissue": "Pancreatic islets",
        "CRISPR_Modality": "CRISPRi",
        "Functional_Justification": "Downregulation of regulatory risk signal"
    },
    {
        "SNP": "rs13266634",
        "Target_Gene": "SLC30A8",
        "Mapping_Rationale": "Coding missense variant in zinc transporter",
        "Tissue": "Pancreatic islets",
        "CRISPR_Modality": "CRISPR knockout",
        "Functional_Justification": "Functional disruption of beta-cell zinc transport"
    },
    {
        "SNP": "rs7172432",
        "Target_Gene": "IRS1",
        "Mapping_Rationale": "Proximal regulatory variant near insulin signaling gene",
        "Tissue": "Pancreatic islets",
        "CRISPR_Modality": "CRISPRi",
        "Functional_Justification": "Regulatory modulation of insulin signaling"
    },
    {
        "SNP": "rs12779790",
        "Target_Gene": "TCF7L2",
        "Mapping_Rationale": "Strong enhancer variant in islet chromatin",
        "Tissue": "Pancreatic islets",
        "CRISPR_Modality": "CRISPRi",
        "Functional_Justification": "Suppression of enhancer-driven TCF7L2 expression"
    }
]

df = pd.DataFrame(data)

# ----------------------------
# Save
# ----------------------------
df.to_csv(OUT_FILE, sep="\t", index=False)

print("✅ Table 3 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
print("\nPreview:")
print(df)
