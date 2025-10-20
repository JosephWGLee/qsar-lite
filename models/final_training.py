#Final training  

from sklearn.ensemble import GradientBoostingRegressor 

def final_training(X_train, y_train, best_params, seed):

    """
    Final training  

    Args:
        seed (int): Random seed for reproducibility  
        X_... (np.ndarray): Molecular feature matrix
        y_... (pd.series): Split solubility values 
        best_params (dict): The best parameters from the optimisation parameter grid  
        
    Returns:
        reg (GradientBoostingRegressor): Final trained model 
    
    """
    
    reg = GradientBoostingRegressor(
        n_estimators=best_params["n_estimators"],
        learning_rate=best_params["learning_rate"],
        max_depth=best_params["max_depth"],
        min_samples_leaf=best_params["min_samples_leaf"],
        min_samples_split=best_params["min_samples_split"],
        subsample=best_params["subsample"],
        random_state=seed
    )
    
    reg.fit(X_train, y_train)

    print("Final model trained on full training data")

    return reg