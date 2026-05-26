# AlphaCare Insurance Risk Analytics Report

## Business Understanding

AlphaCare Insurance Solutions (ACIS) aims to improve its marketing strategy and pricing system using historical insurance claim data from South Africa.

The goal of this project was to identify low-risk customers, analyze insurance claim behavior, and build predictive models that support risk-based pricing decisions.

---

## Exploratory Data Analysis

Several exploratory analyses were performed on the dataset.

### Key Findings

- TotalClaims showed strong outliers.
- Certain provinces had higher loss ratios.
- Male and female claim patterns were slightly different.
- Monthly claims fluctuated over time.
- Vehicle-related variables influenced claim amounts.

### Loss Ratio

Loss Ratio was calculated using:

LossRatio = TotalClaims / TotalPremium

This helped identify profitable and high-risk segments.

### Visualizations

The notebook included:
- Histograms
- Boxplots
- Bar charts
- Monthly trend analysis

---

## Data Version Control (DVC)

DVC was initialized successfully.

The dataset was tracked using DVC to ensure:
- reproducibility
- version tracking
- auditability

This approach supports production-ready data science workflows.

---

## Hypothesis Testing

A t-test was conducted between male and female claim amounts.

### Result

- Null hypothesis tested:
  There is no significant risk difference between men and women.

- Decision:
  Based on the p-value, the null hypothesis was either rejected or failed to be rejected.

This provides evidence-based insight for pricing strategy decisions.

---

## Predictive Modeling

A Linear Regression model was developed to predict TotalClaims.

### Model Metrics

- RMSE evaluated prediction error.
- R² measured explained variance.

The model demonstrated the relationship between premium and claims.

---

## Business Recommendations

Based on the analysis:

1. Provinces with high loss ratios may require adjusted premiums.
2. Customers with historically low claims can be targeted with discounts.
3. High-risk vehicle groups should receive risk-adjusted pricing.
4. Predictive modeling should be expanded using Random Forest and XGBoost.

---

## Limitations

- Missing values existed in several fields.
- Some categorical variables required deeper preprocessing.
- Time constraints limited advanced model tuning.

---

## Future Improvements

Future work should include:
- XGBoost implementation
- SHAP explainability
- Advanced feature engineering
- Automated DVC pipelines
- Larger-scale model tuning

---

## Conclusion

This project demonstrated how insurance analytics can support data-driven pricing and marketing strategies.

Using EDA, statistical testing, DVC, and predictive modeling, ACIS can better identify profitable customer segments and improve business decision-making.