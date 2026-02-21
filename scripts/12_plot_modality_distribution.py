import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/CRISPR_actionability_scores.tsv", sep="\t")

modality_counts = df["Modality"].value_counts()

plt.figure(figsize=(6,5))
modality_counts.plot(kind="bar")

plt.title("CRISPR Modality Assignment")
plt.ylabel("Number of Loci")
plt.xlabel("CRISPR Strategy")

plt.tight_layout()
plt.savefig("figures/high_dpi/Figure6_CRISPR_Modality_Logic.png", dpi=600)
plt.close()

print("Modality figure generated successfully.")
