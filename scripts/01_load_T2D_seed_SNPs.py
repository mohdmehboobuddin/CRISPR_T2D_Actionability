import pandas as pd

df = pd.read_csv("../data/GWAS/T2D_lead_SNPs.tsv", sep="\t")

df.to_csv("../raw_data/T2D_GWAS_raw.csv", index=False)

print("Loaded T2D lead SNPs:", df.shape[0])
print(df)
