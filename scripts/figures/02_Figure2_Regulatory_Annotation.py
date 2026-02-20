import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "results/tables/Table2_Regulatory_Annotation.tsv"

OUT_DIR = BASE_DIR / "figures/high_dpi"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Figure2_Regulatory_Annotation.png"

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(DATA_FILE, sep="\t")

print("📊 Columns found:", list(df.columns))

# ----------------------------
# Define enhancer status
# ----------------------------
df["Enhancer_Status"] = df["Regulatory_Evidence"].apply(
    lambda x: "Enhancer" if "Enhancer" in str(x) else "Non-enhancer"
)

# ----------------------------
# Summarize counts
# ----------------------------
summary = (
    df.groupby(["Variant_Type", "Enhancer_Status"])
      .size()
      .unstack(fill_value=0)
)

# ----------------------------
# Plot
# ----------------------------
summary.plot(
    kind="bar",
    stacked=True,
    figsize=(7, 5)
)

plt.title("Regulatory Annotation of T2D GWAS Variants")
plt.ylabel("Number of SNPs")
plt.xlabel("Variant Type")
plt.xticks(rotation=0)
plt.legend(title="Regulatory Status")

plt.tight_layout()
plt.savefig(OUT_FILE, dpi=400)
plt.close()

print("✅ Figure 2 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
