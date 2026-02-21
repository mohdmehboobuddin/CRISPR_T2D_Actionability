# CRISPR Actionability Framework for Type 2 Diabetes (T2D)

This repository contains the complete computational workflow used to prioritize genome-wide significant Type 2 Diabetes (T2D) loci for modality-specific CRISPR perturbation.

---

## Project Overview

Genome-wide association studies (GWAS) have identified numerous loci associated with T2D risk. Translating these statistical signals into experimentally actionable CRISPR targets requires structured biological prioritization.

The CRISPR Actionability Framework integrates:

- Structural variant classification (coding vs non-coding)
- Pancreatic islet enhancer overlap (H3K27ac)
- Gene transcription start site (TSS) proximity
- Human pancreatic islet RNA-seq expression validation
- Quantitative CRISPR Actionability Scoring (CAS)
- Modality-aware CRISPR assignment (Knockout vs CRISPRi)

The goal is to bridge GWAS discovery with rational CRISPR perturbation strategy design.

---

## Graphical Abstract

<details>
<summary>Click to view graphical abstract (600 DPI)</summary>

<br>

![Graphical Abstract](figures/Graphical_Abstract_T2D_CRISPR_v3.png)

</details>

---

## Repository Structure

data/  
processed_data/  
results/  
figures/  
scripts/  

---

## CRISPR Actionability Score (CAS)

Each locus is evaluated across four components:

1. Genomic Context (0–3)
2. Regulatory Evidence (0–3)
3. Expression Score (0–2)
4. Target Clarity (0–2)

Maximum score: 10  

Priority tiers:

- High Priority: CAS ≥ 7  
- Moderate Priority: CAS 5–6  
- Lower Priority: CAS < 5  

CRISPR modality assignment:

- Coding variants → CRISPR knockout  
- Enhancer-associated non-coding variants → CRISPRi  

---

## Reproducibility

All analyses were performed using Python and BEDTools.

Processed outputs are available in the `results/` directory.

---

## Software and Computational Environment

- Python 3.12
- pandas
- numpy
- matplotlib
- seaborn
- BEDTools (v2.x)

---

## Data Sources

- NHGRI-EBI GWAS Catalog  
- ENCODE pancreatic islet H3K27ac enhancer datasets  
- GENCODE gene annotations  
- GEO pancreatic islet RNA-seq datasets (GSE81608, GSE38642)

Large raw genome annotation files are not hosted in this repository.

---

## Author

Mohd Mehboob Uddin  
Department of Life Sciences  
Osmania University, India  

---

## Citation

If you use this framework, please cite the associated manuscript.

