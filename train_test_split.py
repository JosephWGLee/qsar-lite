import random
from sklearn.model_selection import train_test_split

#Train test split 

def splitting(X, y, smiles):

    seed = 400
    random.seed(seed)
    
    X_train, X_test, y_train, y_test, smiles_train, smiles_test = train_test_split(X, y, smiles, test_size=0.2, random_state=seed)

    return X_train, X_test, y_train, y_test, smiles_train, smiles_test, seed