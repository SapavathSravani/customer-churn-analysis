```python
"""
Telco Customer Churn Analysis - Data Cleaning Pipeline
"""

import pandas as pd
import numpy as np

def clean_churn_data(filepath: str) -> pd.DataFrame:
    # Load dataset
    df = pd.read_csv(filepath)
    
    # 1. Standardize column names
    df.columns = [col.strip() for col in df.columns]
    
    # 2. Convert TotalCharges to numeric & handle blank entries
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].str.strip(), errors='coerce')
    df['TotalCharges'].fillna(df['MonthlyCharges'], inplace=True)
    
    # 3. Format SeniorCitizen indicator
    df['SeniorCitizen'] = df['SeniorCitizen'].map({1: 'Yes', 0: 'No'})
    
    # 4. Feature Engineering: Tenure Grouping for Segmentation
    bins = [0, 12, 24, 48, 60, np.inf]
    labels = ['0-1 Year', '1-2 Years', '2-4 Years', '4-5 Years', '5+ Years']
    df['Tenure_Group'] = pd.cut(df['tenure'], bins=bins, labels=labels, include_lowest=True)
    
    return df

if __name__ == "__main__":
    input_path = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    output_path = "data/cleaned_telco_churn.csv"
    
    df_cleaned = clean_churn_data(input_path)
    df_cleaned.to_csv(output_path, index=False)
    print(f"Data successfully cleaned and saved to {output_path}")
