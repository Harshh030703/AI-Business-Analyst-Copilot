import pandas as pd


def load_data(uploaded_file):
    """
    Load CSV or Excel file into a DataFrame.
    """

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    else:
        return None

    return df


def dataset_summary(df):
    """
    Generate dataset summary statistics.
    """

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Numeric Columns": len(df.select_dtypes(include=["number"]).columns),
        "Categorical Columns": len(df.select_dtypes(include=["object", "category"]).columns),
        "Date Columns": len(df.select_dtypes(include=["datetime64[ns]", "datetime64"]).columns),
        "Memory Usage (MB)": round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2),
    }

    return summary