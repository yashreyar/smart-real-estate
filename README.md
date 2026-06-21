# 🏠 Multimodal Real Estate Valuation Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://smart-real-estate.streamlit.app/)

A data-driven real estate appraisal web application built to estimate residential property values across major Indian micro-markets. The system compounds localized market baselines with custom structural configurations and property age depreciation factors.

---

### 🚀 Live Demo
👉 **[Deploy on Streamlit Cloud](https://smart-real-estate.streamlit.app/)**

---

### 📌 Core Assessment Factors
The engine accurately estimates property values based on:
* **Location Metrics:** Localized market baselines across 15 high-growth Indian residential hubs.
* **Structural Configuration:** Granular layout inputs (Bedrooms, Bathrooms, Furnishing, Floor Levels).
* **Depreciation Matrix:** Property age alignment and structural wear factors.

---

### 🛠️ Tech Stack
* **Language:** Python
* **Modeling & Frameworks:** XGBoost, TensorFlow, Keras, Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Deployment:** Streamlit Cloud

---

### 📊 ML Concepts & Architecture
* **Hybrid Modeling:** Tabular regression (XGBoost) combined with deep learning layers (TensorFlow).
* **Feature Engineering:** Automated pre-processing and pipeline matrices for localized indexing.
* **Granular Appraisal:** Custom component breakdown outputting valuation in Lakhs/Crores.

---

### 📂 Project Structure
```text
smart-real-estate/
├── models/
│   ├── sklearn_pipeline.pkl    # Pre-processing & tabular pipeline matrix
│   └── multimodal_model.h5     # Trained deep learning weight layers
├── src/
│   └── app.py                  # Streamlit application dashboard
└── requirements.txt            # Project dependencies
\* \*\*Asset Valuation Component Matrix:\*\* Dynamically outputs the finalized market appraisal in traditional Indian currency units (Lakhs/Crores) alongside an interactive, scannable baseline metrics breakdown.

\* \*\*Streamlined UI Grid:\*\* Designed with collapsible control drawers to maintain an absolute minimal, user-focused web canvas.



\## 📂 Project Structure

```text

smart-real-estate/

├── models/

│   ├── sklearn\_pipeline.pkl    # Pre-processing \& tabular pipeline matrix

│   └── multimodal\_model.h5     # Trained deep learning weight layers

├── src/

│   └── app.py                  # Streamlit application dashboard

└── requirements.txt            # Project dependencies

