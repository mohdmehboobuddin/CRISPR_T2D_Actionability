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

OUT_FILE = OUT_DIR / "Figure3_SNP_to_TargetGene.png"

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(DATA_FILE, sep="\t")

# Count SNPs per gene
gene_counts = (
    df.groupby("Target_Gene")
      .size()
      .sort_values(ascending=True)
)

# ----------------------------
# Plot
# ----------------------------
plt.figure(figsize=(7, 5))
gene_counts.plot(kind="barh")

plt.title("Mapping of T2D GWAS SNPs to CRISPR Target Genes")
plt.xlabel("Number of GWAS SNPs")
plt.ylabel("Target Gene")

plt.tight_layout()
plt.savefig(OUT_FILE, dpi=400)
plt.close()

print("✅ Figure 3 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
