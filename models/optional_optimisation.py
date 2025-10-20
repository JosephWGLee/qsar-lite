#Optional Optimisation

import numpy as np
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor 
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV, train_test_split

def optional_optimisation(X_train, y_train, seed):

    """
    Splits the molecular feature matrix, corresponding solubility values, and SMILES into train, test and split datasets 

    Args:
        seed (int): Random seed for reproducibility  
        X_... (np.ndarray): Molecular feature matrix
        y_... (pd.series): Split solubility values 
        
    Returns:
        search (RandomizedSearchCV): Fitted randomised search object
        best_params (dict): The best parameters from the optimisation parameter grid  
        best_optimisation_score (Float): The best cross-validation score
    
    """

    #Base regressor 
    reg = GradientBoostingRegressor(random_state=seed)

    #Example optimisation parameters. For exhaustive searches, use a range of values. 
    optimisation_param_grid = {
        "n_estimators": [500],
        "learning_rate": [0.1],
        "max_depth":[7],
        "min_samples_leaf": [4],
        "min_samples_split": [6], 
        "subsample": [0.7]
    }
    
    #Can remove randomised search CV for machines with better GPUS
    search = RandomizedSearchCV(reg, param_distributions= optimisation_param_grid, n_iter=100, cv=3, n_jobs=-1, verbose=2, random_state=seed)
    
    search.fit(X_train, y_train)
    best_params = search.best_params_
    best_optimisation_score = search.best_score_
    
    print(f"Best Training Parametres: {best_params}")
    print(f"Best Training Score: {best_optimisation_score}")

    return search, best_params, best_optimisation_score