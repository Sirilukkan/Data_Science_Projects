# Orchestrating Jobs, Model Registration, and Continuous Deployment with Amazon SageMaker

Amazon SageMaker offers Machine Learning application developers and Machine Learning operations engineers the ability to orchestrate SageMaker jobs and author reproducible Machine Learning pipelines, deploy custom-build models for inference in real-time with low latency or offline inferences with Batch Transform, and track lineage of artifacts. You can institute sound operational practices in deploying and monitoring production workflows, deployment of model artifacts, and track artifact lineage through a simple interface, adhering to safety and best-practice paradigmsfor Machine Learning application development.

The SageMaker Pipelines service supports a SageMaker Machine Learning Pipeline Domain Specific Language (DSL), which is a declarative Json specification. This DSL defines a Directed Acyclic Graph (DAG) of pipeline parameters and SageMaker job steps. The SageMaker Python Software Developer Kit (SDK) streamlines the generation of the pipeline DSL using constructs that are already familiar to engineers and scientists alike.

The SageMaker Model Registry is where trained models are stored, versioned, and managed. Data Scientists and Machine Learning Engineers can compare model versions, approve models for deployment, and deploy models from different AWS accounts, all from a single Model Registry. SageMaker enables customers to follow the best practices with ML Ops and getting started right. Customers are able to standup a full ML Ops end-to-end system with a single API call.

## SageMaker Pipelines

Amazon SageMaker Pipelines support the following activites:

* Pipelines - A Directed Acyclic Graph of steps and conditions to orchestrate SageMaker jobs and resource creation.
* Processing Job steps - A simplified, managed experience on SageMaker to run data processing workloads, such as feature engineering, data validation, model evaluation, and model interpretation.
* Training Job steps - An iterative process that teaches a model to make predictions by presenting examples from a training dataset.
* Conditional step execution - Provides conditional execution of branches in a pipeline.
* Registering Models - Creates a model package resource in the Model Registry that can be used to create deployable models in Amazon SageMaker.
* Creating Model steps - Create a model for use in transform steps or later publication as an endpoint.
* Parameterized Pipeline executions - Allows pipeline executions to vary by supplied parameters.
* Transform Job steps - A batch transform to preprocess datasets to remove noise or bias that interferes with training or inference from your dataset, get inferences from large datasets, and run inference when you don't need a persistent endpoint.

## Layout of the SageMaker ModelBuild Project Template

The template provides a starting point for bringing your SageMaker Pipeline development to production.

```
|-- codebuild-buildspec.yml
|-- CONTRIBUTING.md
|-- pipelines
|   |-- abalone
|   |   |-- evaluate.py
|   |   |-- __init__.py
|   |   |-- pipeline.py
|   |   `-- preprocess.py
|   |-- get_pipeline_definition.py
|   |-- __init__.py
|   |-- run_pipeline.py
|   |-- _utils.py
|   `-- __version__.py
|-- README.md
|-- sagemaker-pipelines-project.ipynb
|-- setup.cfg
|-- setup.py
|-- tests
|   `-- test_pipelines.py
`-- tox.ini
```

A description of some of the artifacts is provided below:
<br/><br/>
Your codebuild execution instructions:
```
|-- codebuild-buildspec.yml
```
<br/><br/>
Your pipeline artifacts, which includes a pipeline module defining the required `get_pipeline` method that returns an instance of a SageMaker pipeline, a preprocessing script that is used in feature engineering, and a model evaluation script to measure the Mean Squared Error of the model that's trained by the pipeline:

```
|-- pipelines
|   |-- abalone
|   |   |-- evaluate.py
|   |   |-- __init__.py
|   |   |-- pipeline.py
|   |   `-- preprocess.py

```

For additional subfolders with code and/or artifacts needed by pipeline, they need to be packaged correctly by the `setup.py` file. For example, to package a `pipelines/source` folder,

* Include a `__init__.py` file within the `source` folder.
* Add it to the `setup.py` file's `package_data` like so:

```
...
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"pipelines.my_pipeline.src": ["*.txt"]},
    python_requires=">=3.6",
    install_requires=required_packages,
    extras_require=extras,
...
```

<br/><br/>
Utility modules for getting pipeline definition jsons and running pipelines:

```
|-- pipelines
|   |-- get_pipeline_definition.py
|   |-- __init__.py
|   |-- run_pipeline.py
|   |-- _utils.py
|   `-- __version__.py
```
<br/><br/>
Python package artifacts:
```
|-- setup.cfg
|-- setup.py
```
<br/><br/>
A stubbed testing module for testing your pipeline as you develop:
```
|-- tests
|   `-- test_pipelines.py
```
<br/><br/>
The `tox` testing framework configuration:
```
`-- tox.ini
```

### A SageMaker Pipeline

The pipeline that we create follows a typical Machine Learning Application pattern of pre-processing, training, evaluation, and conditional model registration and publication, if the quality of the model is sufficient.

![A typical ML Application pipeline](img/pipeline-full.png)

### Getting some constants

We get some constants from the local execution environment.
