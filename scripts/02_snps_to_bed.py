import pandas as pd

df = pd.read_csv("../raw_data/T2D_GWAS_raw.csv")

bed = pd.DataFrame({
    "chrom": "chr" + df["CHR"].astype(str),
    "start": df["POS"] - 1,
    "end": df["POS"],
    "snp": df["SNP"]
})

bed.to_csv("../processed_data/T2D_SNPs.bed",
           sep="\t", index=False, header=False)

print("BED file written:", bed.shape[0], "SNPs")
