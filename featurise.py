import deepchem as dc

def featurise_data(smiles, solubility):

    """
    Converts SMILES strings into molecular fingerprints

    Args:
        smiles (pd.Series or list): SMILES strings
        solubility (pd.Series): Experimental solubility values
        
    Returns:
        X (np.ndarray): Molecular feature matrix
        y (pd.series): Corresponding solubility values
    
    """
    
    featurizer = dc.feat.CircularFingerprint(size=2048, radius=4)
    
    X = featurizer.featurize(smiles)
    y = solubility

    return X, y 