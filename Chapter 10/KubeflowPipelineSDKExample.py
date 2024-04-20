
import kfp
from kfp import dsl

def preprocess_op():
    return dsl.ContainerOp(
        name='Preprocess Data',
        image='my-registry/preprocess:latest',
        command=['python', '/preprocess.py'],
    )

def train_op(data):
    return dsl.ContainerOp(
        name='Train Model',
        image='my-registry/train:latest',
        command=['python', '/train.py'],
        arguments=['--data', data],
    )

@dsl.pipeline(
    name='Sample Pipeline',
    description='An example pipeline that trains and deploys a model.'
)
def sample_pipeline():
    preprocess_task = preprocess_op()
    train_task = train_op(preprocess_task.output)

# Compile the pipeline
pipeline_func = sample_pipeline
pipeline_filename = pipeline_func.__name__ + '.pipeline.zip'

kfp.compiler.Compiler().compile(pipeline_func, pipeline_filename)
