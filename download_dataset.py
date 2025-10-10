import pandas as pd
import deepchem as dc
from rdkit import Chem
import warnings
from rdkit import RDLogger

warnings.filterwarnings("ignore", category=DeprecationWarning)
RDLogger.DisableLog('rdApp.*')

#Importing ESOL Delaney solubility dataset 

def load_data():
    
    tasks, datasets, transformers = dc.molnet.load_delaney(featurizer="GraphConv", splitter="random", reload=False)
    
    train_dataset, valid_dataset, test_dataset = datasets
    
    train_df = train_dataset.to_dataframe()
    valid_df = valid_dataset.to_dataframe()
    test_df = test_dataset.to_dataframe()
    
    smiles_train, sol_train = train_df["ids"], train_df["y"]
    #smiles_test, sol_test = test_df["ids"], test_df["y"]
    #smiles_valid, sol_valid = valid_df["ids"], valid_df["y"]

    return smiles_train, sol_train #(smiles_valid, sol_valid), (smiles_test, sol_test)