import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_FILE = BASE_DIR / "results/tables/Table1_GWAS_SNP_Summary.tsv"
OUT_DIR = BASE_DIR / "figures/high_dpi"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Figure1_GWAS_SNP_Landscape.png"

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(DATA_FILE, sep="\t")

counts = df["Variant_Type"].value_counts()

# ----------------------------
# Plot
# ----------------------------
plt.figure(figsize=(6, 5))
counts.plot(kind="bar")

plt.title("GWAS Variant Landscape for Type 2 Diabetes")
plt.ylabel("Number of SNPs")
plt.xlabel("Variant Type")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(OUT_FILE, dpi=400)
plt.close()

print("✅ Figure 1 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
