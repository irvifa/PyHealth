# ProtoECGNet rhythm branch: MacBook results

**Setup.** PTB-XL 1.0.3, rhythm branch (16 labels, the paper's grouping).
Folds 1–8 / 9 / 10 give train 16,913 / val 2,111 / test 2,108 ECGs; ECGs with
no rhythm label are dropped. 1D ResNet (width 64), global prototypes, 5 per
label (the paper's count), proto_dim 128. Adam, lr 1e-3, batch 32.
`feature_extractor` and `joint` train for 20 epochs each, `classifier` for 15.
Seeds 0, 1 and 2. Device: MacBook Pro M4 Pro (24 GB), MPS. About 53 minutes
of total compute for the 9 runs.

Both prototype variants start from the same per-seed backbone checkpoint and
use the same data order, so they get an equal tuning budget and form a paired
comparison. The black-box is that same backbone with its linear head. AUROC is
computed from logits (see "Projection" below).

## Headline (fold 10, mean ± std over 3 seeds)

| Variant | Macro AUROC | Weighted AUROC | Paper macro |
|---|---|---|---|
| Black-box | 0.9394 ± 0.0030 | 0.9207 ± 0.0019 | 0.9403 |
| No contrastive | 0.9357 ± 0.0026 | 0.9090 ± 0.0018 | 0.8903 |
| Contrastive | 0.9302 ± 0.0046 | 0.8940 ± 0.0030 | 0.9064 |

## H2: contrastive gain under an equal budget

| Seed | No contrastive | Contrastive | Gain | Paired bootstrap 95% CI |
|---|---|---|---|---|
| 0 | 0.9393 | 0.9340 | −0.0053 | [−0.0143, +0.0043] |
| 1 | 0.9333 | 0.9329 | −0.0004 | [−0.0080, +0.0068] |
| 2 | 0.9346 | 0.9237 | −0.0109 | [−0.0191, −0.0030] |

Mean gain −0.0055 ± 0.0043 (seed std). The paper reports +0.0161 from one run
with unequal tuning. The gain is negative in 3 of 3 seeds, and seed 2's CI
excludes 0. **H2 is not supported on the rhythm branch:** with an equal
budget, the contrastive loss slightly hurts macro AUROC, and weighted AUROC
more so (−0.015).

## H3-style margin (branch level, not the 71-label fusion H3)

Black-box − contrastive = +0.0092 ± 0.0043; black-box − no contrastive =
+0.0037. Both are inside the proposal's 0.015 margin. The paper's gap was
+0.0339.

## Comparison with the paper

- **Black-box reproduced:** 0.9394 vs 0.9403 (−0.0009, within one seed std).
- **Both prototype variants beat the paper's numbers** (+0.045 and +0.024).
  One plausible cause is the 15-epoch classifier stage; that is a hypothesis
  and wasn't tested. Other differences: no Optuna, the paper's default loss
  weights, and the branch is trained alone rather than inside the 3-branch
  model.

## Per-label macro AUROC (mean over 3 seeds), sorted by contrastive − no contrastive

| Label | Test positives | Black-box | No contr. | Contr. | Contr. − no contr. |
|---|---|---|---|---|---|
| IVCD | 79 | 0.624 | 0.587 | 0.543 | −0.044 |
| SARRH | 77 | 0.878 | 0.871 | 0.850 | −0.021 |
| AFLT | 7 | 0.953 | 0.965 | 0.948 | −0.017 |
| SR | 1674 | 0.924 | 0.910 | 0.893 | −0.017 |
| 2AVB | 1 | 0.981 | 0.990 | 0.980 | −0.011 |
| 1AVB | 79 | 0.949 | 0.953 | 0.943 | −0.010 |
| SBRAD | 64 | 0.956 | 0.957 | 0.950 | −0.007 |
| PACE | 28 | 0.944 | 0.951 | 0.946 | −0.004 |
| STACH | 82 | 0.994 | 0.991 | 0.989 | −0.002 |
| SVTAC | 3 | 0.995 | 0.997 | 0.996 | −0.000 |
| PSVT | 2 | 0.998 | 0.998 | 0.998 | −0.000 |
| AFIB | 152 | 0.982 | 0.983 | 0.983 | +0.001 |
| TRIGU | 2 | 0.979 | 0.980 | 0.982 | +0.002 |
| BIGU | 8 | 0.954 | 0.954 | 0.958 | +0.005 |
| 3AVB | 2 | 0.998 | 0.982 | 0.997 | +0.015 |
| SVARR | 14 | 0.922 | 0.903 | 0.928 | +0.025 |

The contrastive loss hurts most on IVCD, SARRH and SR, the frequent labels
that co-occur with many others. It helps slightly on a few rare labels
(SVARR, 3AVB, BIGU). Labels with fewer than 10 test positives are noisy.
IVCD is weak for every model (≤ 0.62); it is a conduction (morphology-like)
finding that the paper nonetheless assigns to the rhythm branch.

## Projection (found while setting up this run)

Right after `project_prototypes()`, the rhythm branch's logits drop to about
−100 to −300. Float32 sigmoid then underflows to exactly 0, and AUROC computed
from `y_prob` reads 0.5. The sweep scores logits instead and trains the
classifier for 15 epochs. In a 1-seed probe with a 2-epoch backbone, that
recovered macro AUROC from 0.54 to 0.85.

## Files

`results.jsonl` (raw rows), `summary.md` (generated), `preds/*.npz` (fold-10
labels and logits per run), `checkpoints/` (per-seed backbones), `log.txt`,
`config.json`.
