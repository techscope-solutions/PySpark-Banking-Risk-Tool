# risk_model.py
from pyspark.sql.functions import when

def riskAssessment(df):
    # Simple risk assessment based on income
    # This is just a placeholder logic; you should replace it with your actual model logic
    risk_df = df.withColumn("RiskLevel", when(col("Income") < 50000, "High")
                           .when(col("Income").between(50000, 100000), "Medium")
                           .otherwise("Low"))
    return risk_df
