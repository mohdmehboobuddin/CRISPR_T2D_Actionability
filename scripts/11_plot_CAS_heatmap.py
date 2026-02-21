import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("results/CRISPR_actionability_scores.tsv", sep="\t")

heatmap_data = df[[
    "Genomic_Context",
    "Regulatory_Evidence",
    "Expression_Score",
    "Target_Clarity"
]]

heatmap_data.index = df["SNP"]

plt.figure(figsize=(8,6))
sns.heatmap(heatmap_data, annot=True, cmap="viridis", cbar=True)
plt.title("CRISPR Actionability Score Component Heatmap")
plt.tight_layout()
plt.savefig("figures/high_dpi/Figure7_CRISPR_Prioritization_Heatmap.png", dpi=300)
plt.close()

print("Heatmap generated successfully.")
