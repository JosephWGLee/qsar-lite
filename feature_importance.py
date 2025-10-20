#Feature importance

def feature_importance(reg, X_train, save_path="feature_importance.png"):

    """
    Create a feature importance plot for the training data
    
    Args:

        reg (GradientBoostingRegressor): Final trained model 
        X_train (np.ndarray): Molecular feature matrix

    Returns:

        Nothing 
        
    """
    
    importances = reg.feature_importances_ #GB assigns numerical importance to each feature
    X_train_df = pd.DataFrame(X_train, columns=[f"Feature {i}" for i in range(X_train.shape[1])])
    feature_names = X_train_df.columns
    
    feat_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances}).sort_values('Importance', ascending=False)
    
    plt.figure(figsize=(10,6))
    plt.barh(feat_imp_df['Feature'][:20], feat_imp_df['Importance'][:20])
    plt.gca().invert_yaxis()
    plt.xlabel('Importance')
    plt.title('Top 20 Feature Importances')
    plt.savefig(save_path, dpi=300)
    plt.close()