import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "results/tables/Table4_Islet_Expression_Validation.tsv"

OUT_DIR = BASE_DIR / "figures/high_dpi"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Figure4_Islet_Expression.png"

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(DATA_FILE, sep="\t")

# Sort by expression
df = df.sort_values("Mean_RPKM", ascending=False)

# ----------------------------
# Plot
# ----------------------------
plt.figure(figsize=(8, 5))

bars = plt.bar(
    df["Target_Gene"],
    df["Mean_RPKM"],
)

plt.yscale("log")
plt.ylabel("Mean Expression (RPKM, log scale)")
plt.xlabel("Target Gene")
plt.title("Expression of CRISPR Target Genes in Human Pancreatic Islets")

plt.tight_layout()
plt.savefig(OUT_FILE, dpi=400)
plt.close()

print("✅ Figure 4 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
