# MLOps Pipeline for Wine Quality Prediction

This project demonstrates an end-to-end **MLOps pipeline** for predicting wine quality using the popular dataset from the **UCI Machine Learning Repository**. It covers everything from data ingestion and preprocessing to model training, evaluation, and deployment, with a strong focus on modularity, reproducibility, and automation.

---

## Overview

- **Goal:** Predict wine quality based on physicochemical features using a structured MLOps workflow.
- **Approach:** Modular code structure with reusable components for data processing, model training, and deployment.
- **Deployment:** Flask-based web API for real-time predictions.
- **Tracking & Versioning:** MLflow and DagsHub used for experiment tracking and data/model version control.

---

## Features

- Robust data preprocessing (handling missing values, scaling, encoding)
- Feature engineering and feature selection
- Elastic Net Regression for interpretable model training
- Workflow modularization (pipelines for ingestion, transformation, training, evaluation)
- Model evaluation and experiment tracking with **MLflow**
- Model deployment using **Flask API**
- Integration with **DVC** and **DagsHub** for pipeline reproducibility and collaboration

---

## MLOps Workflow

1. **Data Ingestion**  
   Load raw data and store in version-controlled format.

2. **Data Validation**  
   Perform schema checks and ensure data quality before training.

3. **Data Transformation**  
   Handle preprocessing steps like imputation, scaling, and feature engineering.

4. **Model Training**  
   Train an Elastic Net Regression model with modular pipeline support.

5. **Model Evaluation**  
   Evaluate model using regression metrics; log results to **MLflow**; track dataset/model versions via **DagsHub**.

6. **Model Deployment**  
   Serve predictions using a lightweight **Flask API**.

7. **Prediction Endpoint**  
   Accept user input and return predicted wine quality in real-time.

---

## Future Improvements

- Add support for additional models (e.g., XGBoost, Random Forest, or neural networks).
- Integrate CI/CD with GitHub Actions for automated testing and deployment.
- Add Docker support for containerized reproducible environments.
- Use Streamlit or FastAPI for enhanced UI/UX or performance.
- Integrate monitoring and alerting for deployed models.

---

## License

This project is licensed under the MIT License.
