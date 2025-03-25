## Overview

This project focuses on MLOps for predicting wine quality based on 11 input variables. The project follows a modular coding approach, ensuring code reusability and maintainability. A complete ML pipeline is built and deployed using a Flask web application.

## Features

Data preprocessing (handling missing values, feature scaling, encoding categorical variables if applicable)

Feature engineering and selection

Elastic Net Regression model training and evaluation

Model deployment using Flask

## Dataset

The dataset consists of wine samples with their respective quality scores.

Each sample includes 11 physicochemical attributes such as:

Fixed acidity

Volatile acidity

Citric acid

Residual sugar

Chlorides

Free sulfur dioxide

Total sulfur dioxide

Density

pH

Sulphates

Alcohol

The target variable is Quality, which represents the wine's quality score on a scale.


## Installation

To set up the project, install the required dependencies using:

pip install -r requirements.txt

## Usage

Running the Flask App

python app.py

Then, access the application at http://127.0.0.1:8080/

## Workflows

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW, Dagshub
6. Prediction 

## Future Improvements

Experiment with other machine learning and deep learning models.

## License

This project is licensed under the MIT License.

## Acknowledgments

Kirsh C Naik for the dataset and the tutorial on this project.
