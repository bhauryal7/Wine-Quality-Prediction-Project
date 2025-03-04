from src.DS_Project import logger
from src.DS_Project.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.DS_Project.pipeline.data_validation import DataValidationTrainingPipeline
from src.DS_Project.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.DS_Project.pipeline.model_trainer import ModelTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e 

STAGE_NAME="Data Validation Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e 


STAGE_NAME="Data Transformation Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e 


STAGE_NAME="Model Training Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e 


