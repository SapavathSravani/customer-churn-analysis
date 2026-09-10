# 📊 Customer Churn Analysis & Power BI Dashboard

![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?logo=powerbi)
![Python](https://img.shields.io/badge/Python-EDA%20%26%20Data%20Cleaning-blue?logo=python)
![Status](https://img.shields.io/badge/Project-Completed-success)

## 📌 Project Overview
This project focuses on analyzing customer churn behavior using the **Telco Customer Churn** dataset (7,043 customer records) and developing an interactive **Power BI Dashboard** to identify high-risk customer segments and support proactive retention strategies.

Using Python for exploratory data analysis (EDA) and data transformation, key variables influencing churn—such as contract type, payment method, and tenure—were isolated and visualized in Power BI for actionable executive reporting.

---

## 📸 Dashboard Preview

![Dashboard Overview](screenshots/dashboard_overview.png)

---

## 🎯 Key Business Findings

* **Overall Churn Rate:** **26.54%** across the entire customer base (1,869 churned customers out of 7,043 total).
* **Contract Type Risk:**
  * **Month-to-month:** Highest churn risk at **42.71%**.
  * **One-year:** Moderate risk at **11.27%**.
  * **Two-year:** Extremely low risk at **2.83%**.
* **Payment Method Behavior:**
  * **Electronic check:** Highest churn rate at **45.29%**.
  * **Mailed check:** **19.11%** churn rate.
  * **Bank transfer (automatic):** **16.71%** churn rate.
  * **Credit card (automatic):** **15.24%** churn rate.

---

## 🛠️ Tools & Technologies Used
* **Python (Pandas, NumPy):** Data ingestion, cleaning, standardizing null values, and feature preparation.
* **Power BI:** Data modeling, DAX measures, dynamic filtering, interactive visual charts, and KPI cards.
* **Git & GitHub:** Version control and project documentation.

---

## 📁 Repository Structure

```text
telco-customer-churn-analysis/
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── cleaned_telco_churn.csv
├── dashboard/
│   └── Customer_Churn_Analysis.pbix
├── screenshots/
│   └── dashboard_overview.png
├── src/
│   └── eda_and_cleaning.py
├── .gitignore
├── README.md
└── requirements.txt
