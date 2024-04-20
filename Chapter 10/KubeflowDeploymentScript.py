
import kfp
from kfp import Client
import os

model_image = f"my-model:{os.getenv('BUILD_NUMBER')}"

client = Client(host='http://your-kubeflow-pipelines-endpoint')

pipelines = client.list_pipelines(filter=f"name={pipeline_name}")
pipeline_id = pipelines.pipelines[0].id

client.run_pipeline(pipeline_id, f"deploy-{os.getenv('BUILD_NUMBER')}", {"model-image": model_image})
