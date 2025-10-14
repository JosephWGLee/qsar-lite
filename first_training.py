from sklearn.ensemble import GradientBoostingRegressor 
from sklearn.model_selection import cross_val_score

def first_training(X_train, y_train, seed):

    """
    Initial training of a Gradient Boosting Regressor model

    Args:
        X_train (np.ndarray): Molecular feature matrix
        y_train (pd.series): Corresponding solubility values
        seed (int): random seed for reproducibility 
        
    Returns:
        reg (GradientBoostingRegressor): Initial trained model 
        score (float): The initial cross-validation score 
    
    """

    reg = GradientBoostingRegressor(random_state=seed)
    reg.fit(X_train, y_train)
    
    score=(cross_val_score(reg, X_train, y_train, cv=3, n_jobs=-1).mean())
    return(f"Initial Cross-validation score is: {score}")

    return reg, score 