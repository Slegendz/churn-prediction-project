# Churn Prediction Pipeline: Advanced Machine Learning Workflow

## 📌 Project Overview
This repository contains a full-stack, end-to-end Machine Learning pipeline aimed at predicting customer churn *before* the renewal window concludes. Built around advanced feature engineering, statistical hypothesis testing, and tree-based classification scaling, it provides intervention teams with highly reliable, rank-ordered lists of at-risk clients. 

The pipeline strictly eliminates administrative "data leakage" parameters, ensuring the model focuses purely on genuine human behavioral drivers, CRM engagement metadata, and pricing dynamic thresholds to forecast risk.

---

## 🏗️ Architectural Workflow

The project is gracefully decoupled into distinct, sequential Jupyter Notebooks to simulate production-level lifecycle management.

### 1. **Feature Engineering** (`02_feature_engineering/01_unique_rows_method/01_combining_filtering.ipynb`)
- **Data Intake**: Merges fragmented data objects including interactions, complaints, CRM feedback, and renewal logs.
- **Imputation**: Resolves null spaces across continuous/ordinal matrices.
- **Dynamic Derivations**: 
  - Generates cross-sectional intelligence like `price_change_pct`, `cc_sentiment_delta` (Customer Care call improvement/decline indexing).
  - Rolls logic up into risk flags like `complaint_intensity` and `competitive_pressure`.
- **Output**: Generates `churn_prediction_engineered.csv` and generic validation framework `open_prospects_engineered.csv`.

### 2. **Exploratory Data Analysis** (`01_eda/02_combined_eda.ipynb`)
- Identifies critical distribution insights mathematically and strictly visualizes underlying class variance.
- Validates **12 Real-World Business Hypotheses** against retention outcomes applying strict tests such as **Chi-Square, Mann-Whitney U, and Spearman Correlation** computations.
- Exposes intrinsic customer baselines on the impact of Auto-Renewals, First-Year Tenures, and Hardship triggers.

### 3. **Model Engineering** (`03_modeling/01_train_models.ipynb`)
- Installs automated data leakage purging (actively deleting post-factum identifiers like `payment_timeframe`, `desire_to_cancel_Renewed`, `total_renewal_score_new`).
- Adjusts algorithmic sensitivity to baseline class imbalances (approx ~12% Churn) actively modifying internal `scale_pos_weight` ratios dynamically.
- Tests isolated configurations of **Random Forest, Logistic Regression, & XGBoost**, exporting the winner dynamically to `models/xgb_churn_model.pkl`.

### 4. **Model Evaluation** (`04_evaluation/01_model_evaluation.ipynb`)
- Visualizes Area Under theoretical capabilities via overlapping **Receiver Operating Characteristic (ROC)** benchmarks alongside rigorous **Precision-Recall (PR-AUC)** evaluation matrices optimized against class imbalance misclassification thresholds.

### 5. **Explainability** (`05_explainability/01_shap_analysis.ipynb`)
- Unpacks black-box algorithmic weights using tree-bound explicit SHAP evaluations (`SHapley Additive exPlanations`).
- Identifies top predictors driving probability gradients dynamically via SHAP Partial Dependence modeling. (Key findings mapping retention closely tied to: `tenure_scores`, `sustainability_score`, and pricing variance margins). 

### 6. **Deployment Forecasting** (`03_modeling/02_predict_open_prospects.ipynb`)
- Replaces standard training validations by simulating production streaming. 
- Ingests active (`Open`) renewals without final outcomes, maps identical dynamic feature representations natively via cached frameworks.
- Identifies actionable **High-Risk Intervention Leads** output to `data/processed/open_prospects_churn_predictions.csv` mapped identically against `co_ref` identifications.

### 7. **Pipeline Orchestration & ETL Automation** (`orchestration/`)
- **Automated Runner**: Contains `run_notebooks.ipynb` to programmatically execute pipeline segments sequentially without manual intervention.
- **Data Ingestion Sync**: `data_loading.ipynb` connects securely directly to source raw frameworks.
- **Interim Caching**: Utilizes `interim_data_uploading.ipynb` and `processed_data_uploading.ipynb` to back up all feature engineering transformations to standard data warehouses/cloud instances explicitly.
- **Serialization Store**: Automatically pushes the generated `xgb_churn_model.pkl` to standardized platforms via `model_uploading.ipynb`.

---

## ⚡ Deployment & Running Instructions 

To replicate logic reliably across the framework:

1. **Step 1: Engineering Engine**
   Ensure all original datasets sit securely in your origin paths, then boot and run entirely `02_feature_engineering/01_unique_rows_method/01_combining_filtering.ipynb`. Wait for internal caching generation.
   
2. **Step 2: Analytics Tracking**
   (Optional) Process `01_eda/02_combined_eda.ipynb` to view all correlations interactively inline inline. Wait until `plt.show()` dependencies render matrices successfully.

3. **Step 3: Training Protocols**
   Operate `03_modeling/01_train_models.ipynb`. Confirm mathematical matrices output zero perfect leaks and complete successful `xgb_churn_model.pkl` cache dumps sequentially into `/models`.

4. **Step 4: Diagnostics**
   Iterate `04_evaluation/01_model_evaluation.ipynb` and `05_explainability/01_shap_analysis.ipynb` confirming Recall > ~0.95 and standard Precision outputs tracking properly. 
   
5. **Step 5: Output Generation** 
   Boot `03_modeling/02_predict_open_prospects.ipynb`. Extracts active intervention profiles natively directly outputting sorted metrics CSV files straight back to project origin.
