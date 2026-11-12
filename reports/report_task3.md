# Task 3 Report: AI Agent and Classification Model

| Field | Value |
|---|---|
| Student | Alberto Formigoni |
| Dataset | UCI Bank Marketing |
| Task | Task 3
| Tag / commit | To be added |
| Timebox | partially completed |
| How to run | `uv run python -m ai_mlops_hands_on_exercise.cli` |

## 1. Summary

The objective was to develop an AI assistant capable of answering questions about the Bank Marketing dataset and using a trained machine learning model to predict customer subscriptions.

I trained and evaluated two classification models, Random Forest and MLP, selecting Random Forest based on the positive-class F1-score.

The selected model achieved an **F1-score of approximately 0.46** on the independent test set.

I also developed three Python tools, an initial Claude-based agent and a command-line interface.


## 2. Results

### Model evaluation

| Metric | Random Forest - Test Set |
|---|---:|
| Accuracy | 0.88 |
| F1-score | 0.46 |

On the validation set, Random Forest achieved an F1-score of approximately **0.45**, compared with **0.29** for MLP.

Because only about 11% of customers subscribed, positive-class F1 was prioritized over accuracy.