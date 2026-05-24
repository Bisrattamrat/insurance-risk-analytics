Insurance Risk Analytics & Predictive Modeling

Project Overview

This project analyzes historical insurance claim data for AlphaCare Insurance Solutions (ACIS) to identify low-risk customer segments, optimize pricing strategies, and support data-driven marketing decisions.

The analysis includes:

- Exploratory Data Analysis (EDA)
- Risk and profitability analysis
- Data Version Control (DVC)
- Statistical hypothesis testing
- Predictive modeling
- Risk-based pricing insights

---

Business Objective

The goal is to help ACIS improve insurance pricing and marketing strategy using historical insurance claims data from South Africa.

Key objectives:

- Identify low-risk customer groups
- Analyze claim frequency and severity
- Understand profitability drivers
- Build predictive models for claims and premiums
- Support business decision-making with data insights

---

Project Structure

insurance-risk-analytics/

- .github/workflows/
- data/
- notebooks/
- src/
- tests/
- README.md
- requirements.txt
- dvc.yaml

---

Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- DVC
- GitHub Actions
- Jupyter Notebook

---

Tasks Covered

Task 1

- GitHub setup
- CI/CD workflow
- Exploratory Data Analysis
- Data quality assessment
- Visualization and insights

Task 2

- Data Version Control using DVC

Task 3

- Statistical hypothesis testing

Task 4

- Predictive modeling and pricing analytics

---
Interim Progress

Exploratory Data Analysis Completed

The project currently includes:

- Data quality assessment
- Missing value analysis
- Descriptive statistics
- Loss Ratio calculation
- Geographic risk analysis
- Temporal trend analysis
- Visualization of claims and premium distributions

DVC Setup

Data Version Control (DVC) was initialized to support reproducible and auditable data workflows.

Dataset tracking was configured using DVC for version management.

Key Early Insights

- Certain provinces show higher loss ratios compared to others.
- TotalClaims contains strong outliers that may affect modeling.
- Claim behavior changes over time, suggesting temporal patterns in insurance risk.
## Data Version Control (DVC) after comment 

DVC was initialized to support reproducible data workflows.

The dataset is tracked using DVC instead of Git to avoid storing large raw files directly in the repository.

This setup improves reproducibility, auditability, and scalability for insurance analytics projects.
Author

Developed as part of the 10 Academy Artificial Intelligence Mastery Program – Week 3 Challenge.