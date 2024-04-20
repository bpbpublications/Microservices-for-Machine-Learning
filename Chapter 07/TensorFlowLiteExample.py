
# Convert a TensorFlow model to TensorFlow Lite format
import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model("path_to_saved_model")
tflite_model = converter.convert()

with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
