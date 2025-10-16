#Scatter graph 

import matplotlib.pyplot as plt
import pandas as pd

def scatter_plot(test_dataframe, predicted_RMSE, predicted_r2_score, save_path="scatter_plot.png"):

    """
    Create a scatter plot for the test data
    
    Args:

        test_dataframe (pd.DataFrame): Test dataframe values
        predicted_RMSE (float): Predicted root mean square deviation
        predicted_r2_score (float): Predicted r score 
        save_path (str): File path to scatter plot

    Returns:

        Nothing 
        
    """
    
    min_val = test_dataframe["Actual Solubility logS [mol/L]"].min()
    max_val = test_dataframe["Actual Solubility logS [mol/L]"].max()

    plt.figure(figsize=(6, 6))
    plt.scatter(test_dataframe["Actual Solubility logS [mol/L]"], test_dataframe["Predicted Solubility logS [mol/L]"], s=3) #x, y
    plt.title("Predicted molecular solubility vs measured solubility using gradient boosted trees")
    plt.xlabel("Measured Solubility logS [mol/L]")
    plt.ylabel("Predicted Solubility logS [mol/L]")
    plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--')
    plt.text(0.9, 0.2, 'R-squared = %.3f\nRMSE = %.3f' % (predicted_r2_score, predicted_RMSE))
    plt.savefig(save_path, dpi=300)
    plt.close()