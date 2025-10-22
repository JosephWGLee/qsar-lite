from data.download_dataset import load_data
from features.featurise import featurise_data
from split.train_test_split import splitting
from models.first_training import first_training
from models.optional_optimisation import optional_optimisation
from models.final_training import final_training
from evaluation.dataframe_creation import dataframe_creation
from evaluation.score_calculation import score_calculation 
from evaluation.scatter_plot import scatter_plot
from evaluation.residual_plot import residual_plot
from evaluation.feature_importance import feature_importance

if __name__ == "__main__":
    
    smiles_train, sol_train = load_data()
    X, y = featurise_data(smiles_train, sol_train)
    X_train, X_test, y_train, y_test, smiles_train, smiles_test, seed = splitting(X, y, smiles_train)
    score, reg = first_training(X_train, y_train, seed)
    search, best_params, best_optimisation_score = optional_optimisation(X_train, y_train, seed)
    reg = final_training(X_train, y_train, best_params, seed)
    test_dataframe, train_dataframe = dataframe_creation(reg, X_test, y_test, smiles_test, X_train, y_train, smiles_train)
    predicted_RMSE, predicted_r2_score = score_calculation(test_dataframe)
    scatter_plot(test_dataframe, predicted_RMSE, predicted_r2_score)
    residual_plot(test_dataframe)
    feature_importance(reg, X_train)