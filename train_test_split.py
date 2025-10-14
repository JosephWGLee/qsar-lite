import random
from sklearn.model_selection import train_test_split

#Train test split 

def splitting(X, y, smiles):

    """
    Splits the molecular feature matrix, corresponding solubility values, and SMILES into train, test and split datasets 

    Args:
        X (np.ndarray): Molecular feature matrix
        y (pd.series): Corresponding solubility values
        smiles: SMILES strings from training dataset
        
    Returns:
        X_... (np.ndarray): Molecular feature matrix
        y_... (pd.series): Split solubility values 
    
    """
    
    seed = 400
    random.seed(seed)
    
    X_train, X_test, y_train, y_test, smiles_train, smiles_test = train_test_split(X, y, smiles, test_size=0.2, random_state=seed)

    return X_train, X_test, y_train, y_test, smiles_train, smiles_test, seed