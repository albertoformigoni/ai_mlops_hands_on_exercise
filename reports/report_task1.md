# Task 1 report: Exploratory data analysis



| Field | Value |
| --- | --- |
| Student | Alberto Formigoni |
| Dataset | bank_marketing.zip |
| Task | 1 |
| Tag / commit | [task[N] / short hash] |
| How to run |uv sync then open notebooks/eda.ipynb run all cells using the project's .venv |
| Timebox | finished at 10:15 am |

## 1. Summary

The first task of th project is an exploratory data analysis of a Bank Marketing dataset, containing 41188 observations and 20 features. \
The analysis examines data types and distribution, target class imbalance, numerical correlations, and some visualizations.

The dataset contains 12 duplicate records; furthermore, reading the dataset documentation I discovered that nulla values are labelled "unknown". Additionally, 96.32% of observations used the value 999 in pdays, indicating no previous contact. So I handled this by creating a binary feature called previously_contacted and replacing 999 entries with missing values.

Looking at the correlation analysis, we can see that several economic features such as 'emp.var.rate' and 'euribor3m' are strongly correlated with each other, suggesting potential multicollinearity.\
An important issue spotted is the 'duration' variable, which is positive correlated with the target and probably introduce data leakage; this bebause we cannot know in advance the duration of the call. \
This findings should be taken into attention for the subsequent analysis. 


## 2. Use of AI assistants

| Time  | Purpose                                                  
|-------|----------------------------------------------------------|
| hh:mm | NaN vs "unknown" for `pdays` of never-contacted users    |      |
| hh:mm | Minimal seaborn palette       |      |
| hh:mm | Spearman vs Pearson for correlation                      |      |
| hh:mm | Format the AI usage log table       |      |



