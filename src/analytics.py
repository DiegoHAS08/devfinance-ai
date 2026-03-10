import pandas as pd

def create_dataframe(data):
    df = pd.DataFrame(data, columns=[
        "id", "title", "category", "amount", "date"
    ])
    return df

def expenses_by_category(df):
    return df.groupby("category")["amount"].sum()

def monthly_total(df):
    return df["amount"].sum()