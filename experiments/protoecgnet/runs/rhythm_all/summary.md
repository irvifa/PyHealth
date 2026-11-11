# ProtoECGNet sweep: branch `rhythm`

Fold-10 macro AUROC, mean ± std over seeds (std is 0 when there is only one seed).

| Variant | Seeds | Macro AUROC | Weighted AUROC | Paper macro |
|---|---|---|---|---|
| blackbox | 6 | 0.9368 ± 0.0034 | 0.9178 ± 0.0032 | 0.9403 |
| no_contrastive | 6 | 0.9308 ± 0.0105 | 0.9105 ± 0.0025 | 0.8903 |
| contrastive | 6 | 0.9281 ± 0.0062 | 0.9003 ± 0.0071 | 0.9064 |

## Paired gain from the contrastive loss (H2)

| Seed | No contrastive | Contrastive | Gain | Bootstrap 95% CI |
|---|---|---|---|---|
| 0 | 0.9393 | 0.9340 | -0.0053 | [-0.0143, +0.0043] |
| 1 | 0.9333 | 0.9329 | -0.0004 | [-0.0080, +0.0068] |
| 2 | 0.9346 | 0.9237 | -0.0109 | [-0.0191, -0.0030] |
| 3 | 0.9076 | 0.9313 | +0.0237 | [-0.0082, +0.0548] |
| 4 | 0.9349 | 0.9307 | -0.0042 | [-0.0138, +0.0027] |
| 5 | 0.9349 | 0.9163 | -0.0186 | [-0.0412, +0.0024] |

Mean gain -0.0026 ± 0.0131 (seed std, n=6); paper reports +0.0161 from a single run with unequal tuning.

The per-seed CIs cover test-set sampling only. Seed-to-seed spread is the training-variability estimate.

## Black-box vs ProtoECGNet (H3-style margin)

Black-box − contrastive: +0.0087 ± 0.0056 (proposal margin 0.015; paper gap +0.0339).

## All runs

| branch | seed | variant | val_macro_auroc | test_macro_auroc | test_weighted_auroc | test_labels_scored | test_loss | epochs | classifier_epochs | minutes | device |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rhythm | 0 | blackbox | 0.9527 | 0.9436 | 0.9204 | 16 | 0.4763 | 20 | 15 | 4.6 | mps |
| rhythm | 0 | no_contrastive | 0.9437 | 0.9393 | 0.9095 | 16 | 0.678 | 20 | 15 | 6.6 | mps |
| rhythm | 0 | contrastive | 0.9416 | 0.934 | 0.8898 | 16 | 0.6133 | 20 | 15 | 6.8 | mps |
| rhythm | 1 | blackbox | 0.9545 | 0.9367 | 0.9232 | 16 | 0.6832 | 20 | 15 | 4.4 | mps |
| rhythm | 1 | no_contrastive | 0.9428 | 0.9333 | 0.9065 | 16 | 1.3399 | 20 | 15 | 6.4 | mps |
| rhythm | 1 | contrastive | 0.9528 | 0.9329 | 0.8967 | 16 | 0.7945 | 20 | 15 | 6.6 | mps |
| rhythm | 2 | blackbox | 0.9498 | 0.938 | 0.9186 | 16 | 0.514 | 20 | 15 | 4.4 | mps |
| rhythm | 2 | no_contrastive | 0.9483 | 0.9346 | 0.9109 | 16 | 0.8473 | 20 | 15 | 6.4 | mps |
| rhythm | 2 | contrastive | 0.9456 | 0.9237 | 0.8954 | 16 | 0.6534 | 20 | 15 | 6.6 | mps |
| rhythm | 3 | blackbox | 0.9473 | 0.9349 | 0.9162 | 16 | 0.587 | 20 | 15 | 4.7 | cuda |
| rhythm | 3 | no_contrastive | 0.9425 | 0.9076 | 0.9122 | 16 | 1.5459 | 20 | 15 | 7.6 | cuda |
| rhythm | 3 | contrastive | 0.9473 | 0.9313 | 0.9032 | 16 | 0.8429 | 20 | 15 | 7.8 | cuda |
| rhythm | 4 | blackbox | 0.9457 | 0.9342 | 0.9144 | 16 | 0.5619 | 20 | 15 | 4.8 | cuda |
| rhythm | 4 | no_contrastive | 0.9464 | 0.9349 | 0.9094 | 16 | 0.7518 | 20 | 15 | 7.6 | cuda |
| rhythm | 4 | contrastive | 0.9397 | 0.9307 | 0.9056 | 16 | 0.6642 | 20 | 15 | 7.8 | cuda |
| rhythm | 5 | blackbox | 0.9506 | 0.9337 | 0.9143 | 16 | 0.723 | 20 | 15 | 4.8 | cuda |
| rhythm | 5 | no_contrastive | 0.9536 | 0.9349 | 0.9145 | 16 | 1.1209 | 20 | 15 | 7.7 | cuda |
| rhythm | 5 | contrastive | 0.9476 | 0.9163 | 0.9112 | 16 | 0.9758 | 20 | 15 | 7.8 | cuda |
