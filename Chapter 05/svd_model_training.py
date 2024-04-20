
from surprise import Dataset, SVD, accuracy
from surprise.model_selection import train_test_split
from kfp.components import func_to_container_op

@func_to_container_op
def model_training():
    # Load built-in dataset from surprise library for demonstration
    data = Dataset.load_builtin('ml-100k')
    trainset, testset = train_test_split(data, test_size=.25)
    
    # Use SVD algorithm for training
    algo = SVD()
    
    # Train the model
    algo.fit(trainset)
    
    # Perform predictions
    predictions = algo.test(testset)
    
    # Calculate RMSE (Root Mean Square Error)
    rmse = accuracy.rmse(predictions)
    
    # For a production pipeline, you would save the model to disk or a database here
    
    return f"Model Trained with RMSE: {rmse}"
