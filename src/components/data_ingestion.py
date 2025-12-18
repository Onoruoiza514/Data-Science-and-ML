#Standard Library Imports
import os              # Used for directory and file path handling
import sys             # Used for capturing system-level exception details

#Our Project Specific Imports
from src.exception import CustomException   # Custom exception wrapper
from src.logger import logging              # Centralized logging configuration

#Third Party Imports
import pandas as pd                         # Data handling and manipulation
from sklearn.model_selection import train_test_split  # Dataset splitting
from dataclasses import dataclass            # Cleaner config class

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


#Configuration Class
@dataclass
class DataIngestionConfig:
    """
    Stores all file paths required for data ingestion.
    Using @dataclass removes boilerplate code.
    """
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw_data.csv")


#Data Injestion Component
class DataIngestion:
    """
    Responsible for:
    - Reading raw data
    - Saving raw data
    - Splitting into train/test
    - Saving processed files
    """

    def __init__(self):
        # Initialize ingestion configuration
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Main method that runs the data ingestion pipeline.
        """
        logging.info("Entered the Data Ingestion component")

        try:
            #Read Dataset
            df = pd.read_csv("notebook/student_data.csv")
            logging.info("Dataset read successfully into DataFrame")

            #To create artifacts directory
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            #Saving Raw Data
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )
            logging.info("Raw dataset saved successfully")

            #Spliting Our Datasets Into Test and Train sets
            logging.info("Initiating train-test split")
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

           #Save Training Data
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

           #Saving Test Data
            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info("Data ingestion completed successfully")

            #Return Output Paths
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            #Error Handling
            logging.error("Error occurred during data ingestion", exc_info=True)
            raise CustomException(e, sys)


#Script Test And Entry Point
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
        train_data,
        test_data
    )

model_trainer = ModelTrainer()
print(
    model_trainer.initiate_model_trainer(
        train_arr,
        test_arr,
        preprocessor_path
    )
)
