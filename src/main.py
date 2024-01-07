# main.py
from pyspark.sql import SparkSession
from data_processor import processData
from risk_model import riskAssessment

def main():
    spark = SparkSession.builder.appName("Financial Risk Analysis").getOrCreate()

    # Load data
    data_path = "path/to/your/data.csv"  # Update the path to your data file
    data = spark.read.csv(data_path, header=True, inferSchema=True)

    # Data Preprocessing
    processed_data = processData(data)

    # Risk Assessment
    risk_results = riskAssessment(processed_data)

    # Show results
    risk_results.show()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()
