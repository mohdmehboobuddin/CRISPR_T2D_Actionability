import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "results/tables/Table3_SNP_TargetGene_CRISPR.tsv"

OUT_DIR = BASE_DIR / "figures/high_dpi"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Figure6_SNP_Gene_Pathway.png"

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(DATA_FILE, sep="\t")

# ----------------------------
# Pathway mapping (curated)
# ----------------------------
pathway_map = {
    "KCNJ11": "Insulin Secretion",
    "SLC30A8": "Zinc Transport in β-cells",
    "TCF7L2": "Wnt / β-cell Proliferation",
    "CDKAL1": "tRNA Modification & Insulin Processing",
    "IRS1": "Insulin Signaling",
    "MTNR1B": "Circadian Regulation of Insulin"
}

df["Pathway"] = df["Target_Gene"].map(pathway_map)

# ----------------------------
# Plot
# ----------------------------
plt.figure(figsize=(10, 5))

y_positions = range(len(df))

# SNPs
plt.scatter([0]*len(df), y_positions, s=120, label="GWAS SNPs")
# Genes
plt.scatter([1]*len(df), y_positions, s=120, label="Target Genes")
# Pathways
plt.scatter([2]*len(df), y_positions, s=120, label="Biological Pathways")

# Labels + arrows
for i, row in df.iterrows():
    plt.text(-0.05, i, row["SNP"], ha="right", va="center", fontsize=9)
    plt.text(1.05, i, row["Target_Gene"], ha="left", va="center", fontsize=9)
    plt.text(2.05, i, row["Pathway"], ha="left", va="center", fontsize=9)

    plt.arrow(0.05, i, 0.85, 0, head_width=0.05, length_includes_head=True)
    plt.arrow(1.05, i, 0.85, 0, head_width=0.05, length_includes_head=True)

plt.yticks([])
plt.xticks([0, 1, 2], ["GWAS SNP", "CRISPR Target Gene", "Pathway"])
plt.title("GWAS SNP to CRISPR Target to T2D-Relevant Pathway")

plt.tight_layout()
plt.savefig(OUT_FILE, dpi=400)
plt.close()

print("✅ Figure 6 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
