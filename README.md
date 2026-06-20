\# Multimodal Real Estate Valuation Engine



A data-driven real estate appraisal web application built with Python and Streamlit. The system estimates property values across major Indian micro-markets by compounding localized market baselines with custom structural configurations and property age depreciation factors.



\## 🚀 Live Demo
https://smart-real-estate.streamlit.app/



\## 📊 Features

\* \*\*Localized Pricing Framework:\*\* Calibrated using realistic Q2-2026 market indices across 15 high-growth Indian residential hubs (Delhi-NCR, Mumbai, Bengaluru, Hyderabad, Pune, Chennai, and Kolkata).

\* \*\*Granular Layout Inputs:\*\* Custom parameter inputs for precise configurations including Bedrooms, Halls, Bathrooms, Property Age, Furnishing Status, and Floor Levels (Preferential Location Charges - PLC).

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

