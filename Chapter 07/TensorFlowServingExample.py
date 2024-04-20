
# Assume model is an instance of a trained TensorFlow Keras model
model.save("path_to_saved_model")

# TensorFlow Serving Docker command
docker pull tensorflow/serving
docker run -p 8501:8501 --name=tf_model_serving --mount type=bind,source=/path/to/saved_model/,target=/models/model_name -e MODEL_NAME=model_name -t tensorflow/serving

# Python code to send requests
import requests
import json

data = {
    "signature_name": "serving_default",
    "instances": [{"input_tensor_name": value}]
}
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/model_name:predict', data=json.dumps(data), headers=headers)
predictions = json.loads(json_response.text)['predictions']
