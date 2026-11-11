# ProtoECGNet sweep: branch `rhythm`

Fold-10 macro AUROC, mean ± std over seeds (std is 0 when there is only one seed).

| Variant | Seeds | Macro AUROC | Weighted AUROC | Paper macro |
|---|---|---|---|---|
| blackbox | 3 | 0.9343 ± 0.0005 | 0.9150 ± 0.0009 | 0.9403 |
| no_contrastive | 3 | 0.9258 ± 0.0129 | 0.9120 ± 0.0021 | 0.8903 |
| contrastive | 3 | 0.9261 ± 0.0069 | 0.9067 ± 0.0034 | 0.9064 |

## Paired gain from the contrastive loss (H2)

| Seed | No contrastive | Contrastive | Gain | Bootstrap 95% CI |
|---|---|---|---|---|
| 3 | 0.9076 | 0.9313 | +0.0237 | [-0.0082, +0.0548] |
| 4 | 0.9349 | 0.9307 | -0.0042 | [-0.0138, +0.0027] |
| 5 | 0.9349 | 0.9163 | -0.0186 | [-0.0412, +0.0024] |

Mean gain +0.0003 ± 0.0176 (seed std, n=3); paper reports +0.0161 from a single run with unequal tuning.

The per-seed CIs cover test-set sampling only. Seed-to-seed spread is the training-variability estimate.

## Black-box vs ProtoECGNet (H3-style margin)

Black-box − contrastive: +0.0082 ± 0.0065 (proposal margin 0.015; paper gap +0.0339).

## All runs

| branch | seed | variant | val_macro_auroc | test_macro_auroc | test_weighted_auroc | test_labels_scored | test_loss | epochs | classifier_epochs | minutes | device |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rhythm | 3 | blackbox | 0.9473 | 0.9349 | 0.9162 | 16 | 0.587 | 20 | 15 | 4.7 | cuda |
| rhythm | 3 | no_contrastive | 0.9425 | 0.9076 | 0.9122 | 16 | 1.5459 | 20 | 15 | 7.6 | cuda |
| rhythm | 3 | contrastive | 0.9473 | 0.9313 | 0.9032 | 16 | 0.8429 | 20 | 15 | 7.8 | cuda |
| rhythm | 4 | blackbox | 0.9457 | 0.9342 | 0.9144 | 16 | 0.5619 | 20 | 15 | 4.8 | cuda |
| rhythm | 4 | no_contrastive | 0.9464 | 0.9349 | 0.9094 | 16 | 0.7518 | 20 | 15 | 7.6 | cuda |
| rhythm | 4 | contrastive | 0.9397 | 0.9307 | 0.9056 | 16 | 0.6642 | 20 | 15 | 7.8 | cuda |
| rhythm | 5 | blackbox | 0.9506 | 0.9337 | 0.9143 | 16 | 0.723 | 20 | 15 | 4.8 | cuda |
| rhythm | 5 | no_contrastive | 0.9536 | 0.9349 | 0.9145 | 16 | 1.1209 | 20 | 15 | 7.7 | cuda |
| rhythm | 5 | contrastive | 0.9476 | 0.9163 | 0.9112 | 16 | 0.9758 | 20 | 15 | 7.8 | cuda |
