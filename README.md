# CRISPR Actionability Framework for Type 2 Diabetes (T2D)

This repository contains the computational workflow used to prioritize genome-wide significant Type 2 Diabetes (T2D) loci for modality-specific CRISPR perturbation.

## Project Overview

The CRISPR Actionability Framework integrates:

- Structural variant classification
- Pancreatic islet enhancer overlap (H3K27ac)
- Gene transcription start site (TSS) proximity
- Islet RNA-seq expression validation
- Quantitative CRISPR Actionability Scoring (CAS)

The goal is to translate GWAS loci into experimentally actionable CRISPR targets.

---

## Repository Structure

data/               → Public reference metadata (no large raw files)  
processed_data/     → Processed SNP and annotation intersections  
results/            → Final scoring tables and expression validation outputs  
figures/            → Publication-ready figures  
scripts/            → Python scripts for full reproducible workflow  

---

## Reproducibility

All analyses were performed using Python and BEDTools.

Main workflow steps:

1. Load curated T2D GWAS SNPs  
2. Convert SNPs to BED format  
3. Expand ±50kb regulatory windows  
4. Intersect with pancreatic islet enhancers  
5. Extract gene TSS coordinates  
6. Validate islet gene expression  
7. Compute CRISPR Actionability Score (CAS)  

Processed outputs are available in the `results/` directory.

---

## Data Sources

Public datasets used:

- GWAS meta-analysis summary statistics
- ENCODE pancreatic islet H3K27ac enhancer data
- GENCODE gene annotations
- GEO human pancreatic islet RNA-seq datasets (GSE81608, GSE38642)

Due to file size constraints, large raw annotation files are not hosted in this repository and should be downloaded from their respective public sources.

---

## Author

Mohd Mehboob Uddin  
Department of Life Sciences  
Osmania University, India  

---

## Citation

If you use this framework, please cite the associated manuscript.
