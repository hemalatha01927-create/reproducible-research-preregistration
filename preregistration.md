# Analysis Preregistration

**Project title:** Student Study Time and Academic Performance Analysis  
**Version:** 1.0  
**Registration date:** [Enter date before inspecting real outcome data]  
**Researcher:** [Enter your name]  
**Status:** Planned — no real outcome data inspected

## 1. Research question
Among students observed during one examination period, is average daily study time associated with examination score?

## 2. Population
Students who have valid daily study-time and examination-score records for the selected examination period. The target population and institution must be specified before real data collection or analysis.

## 3. Exposure
Average self-reported or recorded study time in hours per day during the defined observation window.

## 4. Comparator
For a descriptive comparison, compare students studying less than 2 hours per day with students studying 2 or more hours per day. The continuous study-time measure will also be analysed to avoid relying only on a threshold.

## 5. Outcome
Examination score, measured in percentage points from 0 to 100. If the source uses another scale, document the conversion before analysis.

## 6. Observation window
The study period immediately preceding one specified examination. Record exact start and end dates before analysing outcomes.

## 7. Hypotheses
- **Null hypothesis (H0):** Study time has no linear association with examination score in the target sample (correlation = 0).
- **Alternative hypothesis (H1):** Study time has a positive association with examination score (correlation > 0).

This is a planned hypothesis, not a claim that the relationship is causal.

## 8. Inclusion rules
- A participant has a valid study-time value of 0 hours or more.
- A participant has a valid examination score from 0 to 100.
- Records belong to the prespecified observation window.
- Use one record per student for the specified examination, unless a different unit is explicitly justified before analysis.

## 9. Exclusion rules
- Missing study-time or examination-score values for the primary analysis.
- Impossible values (study time below 0 or above 24 hours per day; score below 0 or above 100).
- Duplicate records for the same student and examination, resolved using a rule documented before outcome analysis.

Report the number of records excluded for each reason.

## 10. Data transformations
- Preserve an untouched copy of the source data in `data/raw/`.
- Create a cleaned copy in `data/processed/`.
- Convert study time and score to numeric types.
- Do not impute missing primary exposure or outcome values in the primary analysis.
- Retain study time as a continuous variable for the primary analysis.
- Create the <2 hours versus >=2 hours groups only for the planned descriptive comparison.

## 11. Primary statistical analysis
- Report sample size, mean, standard deviation, median, and range for study time and exam score.
- Estimate Pearson correlation between study time and score when the assumptions are reasonable; also report Spearman rank correlation as a robustness check.
- Use a one-sided significance level of 0.05 for the prespecified positive-association hypothesis.
- Report the correlation estimate and a 95% confidence interval where supported by the chosen software/method.
- Interpret the result as association, not proof that study time causes higher scores.

## 12. Effect size
The primary effect size is the Pearson correlation coefficient, reported with its 95% confidence interval. Also report the difference in mean scores between the two planned study-time groups, with a confidence interval if feasible.

## 13. Robustness checks
- Compare Pearson and Spearman correlation estimates.
- Repeat the descriptive summary after excluding records flagged as potential data-entry errors, with the exclusions clearly listed.
- If the sample is too small or assumptions are unsuitable, report this and avoid overstating inference.

## 14. Missing data
Report missingness for each key variable. The primary analysis uses complete cases for study time and exam score. Do not silently drop records; document counts and reasons.

## 15. Reproducibility and output contract
The pipeline must:
- accept a tabular dataset with `study_hours` and `exam_score` columns;
- reject missing required columns;
- flag impossible values;
- return a summary containing `n`, `mean_study_hours`, `mean_exam_score`, and `pearson_correlation` (correlation may be unavailable for insufficient or constant data);
- write no personal identifiers into reports.

## 16. Synthetic pipeline test
Before using real data, run automated tests on a tiny synthetic fixture created only to check code behaviour. The test checks required output fields, valid ranges, and error handling. Synthetic test results must not be presented as research findings.

## 17. Deviations and amendments
Any change after access to real outcome data must be logged below with date, reason, and impact. Do not overwrite the original preregistration.

| Date | Change | Reason | Impact |
|---|---|---|---|
| [Date] | No changes yet | — | — |
