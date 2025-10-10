import deepchem as dc

#Featurise data

def featurise_data(smiles, solubility):
    
    featurizer = dc.feat.CircularFingerprint(size=2048, radius=4)
    
    X = featurizer.featurize(smiles)
    y = solubility

    return X, y 