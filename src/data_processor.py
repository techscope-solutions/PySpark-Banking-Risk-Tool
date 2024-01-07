# data_processor.py
from pyspark.sql.functions import col

def processData(df):
    # Example of data preprocessing steps
    # Let's say you want to filter out customers with a credit score lower than 500
    filtered_df = df.filter(col("CreditScore") >= 500)
    return filtered_df
