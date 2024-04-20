
import logging

def log_prediction(request_data, prediction):
    logging.info(f"Request data: {request_data}")
    logging.info(f"Model prediction: {prediction}")

# Later in the code, after making a prediction:
log_prediction(request_data, model_prediction)
