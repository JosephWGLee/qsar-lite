#Creating dataframes

import pandas as pd

def dataframe_creation(reg, x_test, y_test, smiles_test, X_train, y_train, smiles_train):

    """
    Creates a datarame for the trained and test data 

    Args:

        reg (GradientBoostingRegressor): Final trained model
        smiles_train: SMILES strings from training dataset
        smiles_test: SMILES strings from test dataset 
        X_... (np.ndarray): Molecular feature matrix
        y_... (pd.series): Split solubility values 
        
    Returns:
        test_dataframe (pd.series): Test dataframe values
        train_dataframe (pd.series): Train dataframe values 
    
    """
    
    def build_df(X, y, smiles):
        preds = reg.predict(X)
        residuals = preds - y 
        return pd.DataFrame({"SMILES":smiles, 
                             "Actual Solubility logS [mol/L]": y,
                             "Predicted Solubility logS [mol/L]": preds,
                             "Residuals": residuals
                            })

    train_dataframe = build_df(X_train, y_train, smiles_train)
    test_dataframe = build_df(X_test, y_test, smiles_test)
                             
    return test_dataframe, train_dataframe