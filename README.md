cat << 'EOF' > README.md
# CRISPR Actionability Framework for Type 2 Diabetes (T2D)

This repository contains the complete computational workflow used to prioritize genome-wide significant Type 2 Diabetes (T2D) loci for modality-specific CRISPR perturbation.

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

## Repository Structure

data/               → Public reference metadata (no large raw genome files)  
processed_data/     → Processed SNP annotations and genomic intersections  
results/            → CAS scoring tables and final prioritization outputs  
figures/            → Publication-ready figures (high resolution)  
scripts/            → Full reproducible Python workflow  

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

## Reproducibility

All analyses were performed using Python and BEDTools.

### Main Workflow Steps

1. Load curated T2D GWAS SNPs  
2. Convert SNPs to BED format  
3. Expand ±50 kb regulatory windows  
4. Intersect with pancreatic islet enhancers  
5. Extract gene TSS coordinates  
6. Validate pancreatic islet gene expression  
7. Compute CRISPR Actionability Score (CAS)  
8. Generate final tables and figures  

Processed outputs are available in the results/ directory.

## Software and Computational Environment

Analyses were performed using:

- Python 3.12
- pandas
- numpy
- matplotlib
- seaborn
- BEDTools (v2.x)

Recommended setup:

python3 -m venv crispr_env  
source crispr_env/bin/activate  
pip install pandas numpy matplotlib seaborn  

Install BEDTools (Ubuntu):

sudo apt install bedtools  

All scripts were executed in a Linux (Ubuntu) environment.

## Data Sources

Public datasets used:

- NHGRI-EBI GWAS Catalog  
- ENCODE pancreatic islet H3K27ac enhancer datasets  
- GENCODE gene annotations  
- GEO human pancreatic islet RNA-seq datasets:
  - GSE81608
  - GSE38642

Due to GitHub file size limits, large raw genome annotation files are not hosted in this repository and should be downloaded from their original public sources.

## Author

Mohd Mehboob Uddin  
Department of Life Sciences  
Osmania University, India  

## Citation

If you use this framework, please cite the associated manuscript.

EOF
