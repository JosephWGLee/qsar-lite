# QSAR-Lite

## Overview
This repository contains a QSAR-Lite, a learning project which predicts molecular solubility (logS) of small molecules from their chemical structure using gradient boosted trees. Here, RDKit and DeepChem have been used to featurise SMILES data from the ESOL/Delaney solubility dataset. The gradient boosting ensemble learning algorithm has been used to predict solubility from the featurised SMILES data. This supervised machine learning method has been validated using train-test-split from scikit-learn to simulate how models perform on new data. Optional optimisation for hyperparameter tuning has been provided, as well as graphical representations of the data. 

For me, the aim of this project was to get myself comfortable writing “production-like” code, getting more comfortable with refactoring, tidying, and commenting code in a way that is more easily reproducible and understandable. I also wanted to continue to learn, code, and develop my skills in data handling, ML and Git with a simple and interpretable project. From this project, I have learnt the importance of planning to manage the structure and flow of the project, something I have definitely neglected in my academic work, where just getting it working is my main priority. 

## Repository Structure

- **Data**: Python script for downloading the ESOL/Delaney dataset and processing it.
  
- **Features**: Python script for featurising the SMILES data.
  
- **Split**: Python script for splitting the data into training and test subsets.
  
- **Models**: Python scripts for the initial training of the model, optional optimisation (Very demanding even with a good quality commercial GPU), and the final training model.
  
- **Evaluation**: Python scripts for dataframe creation, score calculation (RMSE, R2) and plots for assessing the feature importance, residuals and the comparison between the predicted solubility and the actual molecular solubility of the tested molecules. Includes example plots.
  
- **Notebooks**: Complete Jupyter notebook for the project.
  
- **main.py**: Script for running the project.
  
- **Requirements**: Requirements for the project. Python 3.9.23.  

## References

1. Delaney J. S. (2004). ESOL: estimating aqueous solubility directly from molecular structure. Journal of chemical information and computer sciences, 44(3), 1000–1005. https://doi.org/10.1021/ci034243x
