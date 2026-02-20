import pandas as pd

# Load hg38 SNPs
df = pd.read_csv(
    "../processed_data/T2D_noncoding_SNPs_hg38.bed",
    sep="\t",
    header=None,
    names=["chrom", "start", "end", "snp"]
)

WINDOW = 50000  # 50 kb

df["win_start"] = (df["start"] - WINDOW).clip(lower=0)
df["win_end"] = df["end"] + WINDOW

windows = df[["chrom", "win_start", "win_end", "snp"]]

windows.to_csv(
    "../processed_data/T2D_noncoding_windows_50kb.bed",
    sep="\t",
    index=False,
    header=False
)

print("Created windows for", windows.shape[0], "SNPs")
