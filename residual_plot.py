#Residual Plot 

def residual_plot(test_dataframe, save_path="residual_plot.png"):

    """
    Create a residual plot for the test data
    
    Args:

        test_dataframe (pd.DataFrame): Test dataframe values 
        save_path (str): File path to residual plot

    Returns:

        Nothing 
        
    """
    
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=test_dataframe["Predicted Solubility logS [mol/L]"], y=test_dataframe["Residuals"])
    plt.title("Residual Plot")
    plt.xlabel("Predicted Solubility logS [mol/L]")
    plt.ylabel("Residuals (Predicted - Actual)")
    plt.axhline(0, color='red', linestyle='--')
    plt.savefig(save_path, dpi=300)
    plt.close()