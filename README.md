---

## CRISPR Actionability Score (CAS)

Each locus is evaluated across four components:

1. **Genomic Context (0–3)**
2. **Regulatory Evidence (0–3)**
3. **Expression Score (0–2)**
4. **Target Clarity (0–2)**

Maximum score: 10  
Priority tiers:

- High Priority: CAS ≥ 7  
- Moderate Priority: CAS = 5–6  
- Lower Priority: CAS < 5  

CRISPR modality is assigned based on genomic architecture:

- Coding variants → CRISPR knockout  
- Enhancer-associated non-coding variants → CRISPR interference (CRISPRi)

---

## Reproducibility

All analyses were performed using Python and BEDTools.

### Main Workflow Steps

1. Load curated T2D GWAS SNPs
2. Convert SNPs to BED format
3. Expand ±50 kb regulatory windows
4. Intersect with pancreatic islet H3K27ac enhancers
5. Extract gene TSS coordinates
6. Validate pancreatic islet gene expression
7. Compute CRISPR Actionability Score (CAS)
8. Generate prioritization tables and figures

Processed outputs are available in the `results/` directory.

---

## Software and Computational Environment

Analyses were performed using:

- Python 3.12
- pandas
- numpy
- matplotlib
- seaborn
- BEDTools (v2.x)

### Recommended Setup

```bash
python3 -m venv crispr_env
source crispr_env/bin/activate
pip install pandas numpy matplotlib seaborn
