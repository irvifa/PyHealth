# ProtoECGNet sweep: branch `rhythm`

Fold-10 macro AUROC, mean ± std over seeds (std is 0 when there is only one seed).

| Variant | Seeds | Macro AUROC | Weighted AUROC | Paper macro |
|---|---|---|---|---|
| blackbox | 3 | 0.9394 ± 0.0030 | 0.9207 ± 0.0019 | 0.9403 |
| no_contrastive | 3 | 0.9357 ± 0.0026 | 0.9090 ± 0.0018 | 0.8903 |
| contrastive | 3 | 0.9302 ± 0.0046 | 0.8940 ± 0.0030 | 0.9064 |

## Paired gain from the contrastive loss (H2)

| Seed | No contrastive | Contrastive | Gain | Bootstrap 95% CI |
|---|---|---|---|---|
| 0 | 0.9393 | 0.9340 | -0.0053 | [-0.0143, +0.0043] |
| 1 | 0.9333 | 0.9329 | -0.0004 | [-0.0080, +0.0068] |
| 2 | 0.9346 | 0.9237 | -0.0109 | [-0.0191, -0.0030] |

Mean gain -0.0055 ± 0.0043 (seed std, n=3); paper reports +0.0161 from a single run with unequal tuning.

The per-seed CIs cover test-set sampling only. Seed-to-seed spread is the training-variability estimate.

## Black-box vs ProtoECGNet (H3-style margin)

Black-box − contrastive: +0.0092 ± 0.0043 (proposal margin 0.015; paper gap +0.0339).

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
