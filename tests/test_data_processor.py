# Import necessary testing libraries
import unittest
from pyspark.sql import SparkSession
from src.data_processor import processData

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.appName("TestSession").getOrCreate()

    def test_processData(self):
        # Mock data creation
        test_data = self.spark.createDataFrame([
            (1, 50000, 10000, 'Good', 700),
            (2, 45000, 15000, 'Average', 650)
        ], ['CustomerId', 'Income', 'Debt', 'PaymentHistory', 'CreditScore'])

        # Test processData function
        processed_data = processData(test_data)
        self.assertIsNotNone(processed_data)

    def tearDown(self):
        self.spark.stop()

if __name__ == '__main__':
    unittest.main()
