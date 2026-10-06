"""Draw the README charts from numbers printed in NLP_Chatbot.ipynb's saved outputs.

    pip install matplotlib && python scripts/make_charts.py
"""
from pathlib import Path

import matplotlib.pyplot as plt

DOCS = Path(__file__).resolve().parents[1] / "docs"
BLUE, ORANGE, GRAY, INK, MUTED = "#2a78d6", "#eb6834", "#8a8984", "#0b0b0b", "#52514e"

plt.rcParams.update({
    "font.size": 11, "axes.edgecolor": "#d6d5d0", "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False,
    "axes.spines.right": False, "axes.grid": True, "grid.color": "#ecebe7",
    "axes.axisbelow": True, "figure.facecolor": "white", "axes.titleweight": "bold",
    "axes.titlecolor": INK,
})

# Scores after 3 epochs (notebook cell "eval_results = trainer.evaluate()"). Note: eval_dataset was
# train[:600], a subset of the 2,000 training rows, so these are scores on seen examples.
ROUGE = {"ROUGE-1": 0.3947, "ROUGE-2": 0.1789, "ROUGE-L": 0.3598}
# Length statistics (notebook cells after the histograms) and the tokenizer limit used for training
AVG_INSTRUCTION_WORDS, AVG_RESPONSE_WORDS, MAX_TOKENS = 8.69, 112.66, 16

fig, ax = plt.subplots(figsize=(7, 2.6))
names = list(ROUGE)[::-1]
bars = ax.barh(names, [ROUGE[n] for n in names], color=BLUE, height=0.55)
for b, n in zip(bars, names):
    ax.text(ROUGE[n] + 0.01, b.get_y() + b.get_height() / 2, f"{ROUGE[n]:.2f}", va="center", color=INK)
ax.set_xlim(0, 1)
ax.grid(axis="y", visible=False)
ax.set(xlabel="Overlap with the reference reply (0 = none, 1 = identical)",
       title="T5-small ROUGE, scored on 600 training examples")
fig.tight_layout()
fig.savefig(DOCS / "rouge_scores.png", dpi=150)

fig, ax = plt.subplots(figsize=(7, 2.6))
labels = ["Customer message (avg)", "Training limit for replies", "Reference reply (avg)"]
values = [AVG_INSTRUCTION_WORDS, MAX_TOKENS, AVG_RESPONSE_WORDS]
bars = ax.barh(labels[::-1], values[::-1], color=[GRAY, ORANGE, GRAY], height=0.55)
units = ["words", "tokens", "words"][::-1]
for b, v, u in zip(bars, values[::-1], units):
    ax.text(v + 1.5, b.get_y() + b.get_height() / 2, f"{v:.0f} {u}", va="center", color=INK)
ax.set_xlim(0, 135)
ax.grid(axis="y", visible=False)
ax.set(xlabel="Length", title="Replies capped at 16 tokens vs. 113-word references")
fig.tight_layout()
fig.savefig(DOCS / "length_budget.png", dpi=150)
print("wrote docs/rouge_scores.png, docs/length_budget.png")
