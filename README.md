# Churn Prediction Project

This project focuses on predicting customer churn. The goal is to identify customers who are likely to leave the service, allowing the company to take proactive measures to retain them.

## 🛠️ How to Work on This Project (Team Guide)

### 1. Setup (Do this once)

```bash
git clone <repo-url>
cd churn-prediction-project

python -m venv venv
```

Activate environment:

* Windows:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

---

### 2. Add Dataset

Put all dataset files inside:

```
data/raw/
```

(Files are shared separately in ZIP)

---

### 3. Where to Work

* **EDA work** → `notebooks/01_eda.ipynb`
* **Feature engineering** → `notebooks/02_feature_engineering.ipynb`
* **Model building** → `notebooks/03_modeling.ipynb`
* **Evaluation** → `notebooks/04_evaluation.ipynb`
* **Explainability + insights** → `notebooks/05_explainability.ipynb`

👉 Don’t mix work in random files.

---

### 4. Workflow (Important)

Follow this order:

```
EDA → Feature Engineering → Modeling → Evaluation → Explainability
```

Save outputs properly:

* Clean data → `data/interim/`
* Final dataset → `data/processed/`
* Models → `outputs/models/`
* Graphs → `outputs/figures/`

---

### 5. Rules

* Don’t modify files in `data/raw/`
* Write clean code (add comments)
* Push regularly to Git
* Don’t upload datasets/models to Git

---

### 6. Before Final Submission

* All notebooks should run without errors
* Outputs should be saved
* PPT + docs should be updated

---
