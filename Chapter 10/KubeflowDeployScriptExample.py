
import kfp
from kfp import Client

model_image = f"my-model:{CI_COMMIT_REF_SLUG}"

client = Client(host='http://your-kubeflow-pipelines-endpoint')

pipelines = client.list_pipelines(filter=f"name={pipeline_name}")
pipeline_id = pipelines.pipelines[0].id

client.run_pipeline(pipeline_id, 'deploy', {"model-image": model_image})
