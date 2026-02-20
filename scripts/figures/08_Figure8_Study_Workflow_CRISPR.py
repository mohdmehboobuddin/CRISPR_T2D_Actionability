import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Arrow
from pathlib import Path

# ----------------------------
# Output path
# ----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
OUT_DIR = BASE_DIR / "figures/high_dpi"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_FILE = OUT_DIR / "Figure8_Study_Workflow_CRISPR.png"

# ----------------------------
# Helper function
# ----------------------------
def draw_box(ax, xy, width, height, text):
    box = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.03",
        linewidth=1.5
    )
    ax.add_patch(box)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=11,
        wrap=True
    )

# ----------------------------
# Create figure
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

# ----------------------------
# Draw workflow boxes
# ----------------------------
draw_box(
    ax,
    (0.5, 3.5),
    2.6,
    1.2,
    "Type 2 Diabetes GWAS SNPs\n(Genome-wide association studies)"
)

draw_box(
    ax,
    (3.6, 3.5),
    2.8,
    1.2,
    "Functional Annotation\n• Coding vs Noncoding\n• Enhancers\n• Regulatory context"
)

draw_box(
    ax,
    (6.9, 3.5),
    2.6,
    1.2,
    "Target Gene Mapping\nSNP → Gene assignment\nusing genomic context"
)

draw_box(
    ax,
    (2.0, 1.5),
    3.2,
    1.3,
    "Pancreatic Islet Expression Validation\n(RNA-seq evidence)"
)

draw_box(
    ax,
    (6.0, 1.5),
    3.2,
    1.3,
    "CRISPR Strategy Selection\nCRISPRi / CRISPRa / Knockout"
)

# ----------------------------
# Draw arrows
# ----------------------------
ax.annotate("", xy=(3.6, 4.1), xytext=(3.1, 4.1), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(6.9, 4.1), xytext=(6.4, 4.1), arrowprops=dict(arrowstyle="->", lw=1.5))

ax.annotate("", xy=(4.2, 2.8), xytext=(4.2, 3.5), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(6.6, 2.8), xytext=(7.4, 3.5), arrowprops=dict(arrowstyle="->", lw=1.5))

# ----------------------------
# Title
# ----------------------------
ax.text(
    5,
    5.4,
    "Integrated Framework for CRISPR Target Prioritization in Type 2 Diabetes",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold"
)

# ----------------------------
# Save
# ----------------------------
plt.tight_layout()
plt.savefig(OUT_FILE, dpi=400)
plt.close()

print("🏁 Figure 8 generated successfully")
print(f"📁 Saved to: {OUT_FILE}")
