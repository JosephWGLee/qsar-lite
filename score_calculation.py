#Calculating Scores

from sklearn.metrics import root_mean_squared_error, r2_score

def score_calculation(test_dataframe):

    """
    Calculate RMSE and R2 scores for the test_dataframe 
    
    Args:

        test_dataframe (pd.DataFrame): Test dataframe values

    Returns:
        predicted_RMSE (float): Predicted root mean square deviation
        predicted_r2_score (float): Predicted r score 
    
    """
    
    predicted_RMSE = root_mean_squared_error(test_dataframe["Actual Solubility logS [mol/L]"], test_dataframe["Predicted Solubility logS [mol/L]"])
    predicted_r2_score = r2_score(test_dataframe["Actual Solubility logS [mol/L]"], test_dataframe["Predicted Solubility logS [mol/L]"])
    
    print(f"The predicted RMSE is: {predicted_RMSE}")
    print(f"The predicted R2 score is: {predicted_r2_score}")

    return predicted_RMSE, predicted_r2_score