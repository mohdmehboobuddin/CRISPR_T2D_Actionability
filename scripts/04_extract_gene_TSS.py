import pandas as pd

genes = []

with open("../data/genes/gencode.v44.basic.annotation.gtf") as f:
    for line in f:
        if line.startswith("#"):
            continue
        parts = line.strip().split("\t")
        if parts[2] == "gene":
            chrom = parts[0]
            start = int(parts[3]) - 1
            end = int(parts[4])
            strand = parts[6]

            info = parts[8]
            gene_name = None
            for field in info.split(";"):
                if "gene_name" in field:
                    gene_name = field.split('"')[1]

            if gene_name:
                tss = start if strand == "+" else end
                genes.append([chrom, tss, tss + 1, gene_name])

df = pd.DataFrame(genes, columns=["chrom", "start", "end", "gene"])
df.to_csv("../processed_data/gene_TSS_hg38.bed",
          sep="\t", index=False, header=False)

print("Extracted TSS for", df.shape[0], "genes")
