## MLOps with Azure Machine Learning (Classical Machine Learning)

This repository is a collection of MLOps sample codes using Azure Machine Learning and GitHub technologies. The type of machine learning algorithm used is Microsoft LightGBM.

## Architecture



### CI/CD Pipeline

|Stages     |Pipeline Type                               |Status          |Description     |
|-----------|--------------------------------------------|----------------|----------------|
|Inner Loop |n/a                                         |                |                |
|Middle Loop|[Training model with MLflow logging](./.github/workflows/ci-pipeline.yml)      |[![middle-loop continuous integration](https://github.com/konabuta/mlops-azureml/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/ci-pipeline.yml)|Run reproducible model training pipeline.|
|Outer Loop |[Continuous Deployment](./.github/workflows/cd-pipeline.yml)                       |[![outer-loop continuous deployment](https://github.com/konabuta/mlops-azureml/actions/workflows/cd-pipeline.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/cd-pipeline.yml)|Run reproducible model deployment pipeline into Stage & Prod environments.|
|           |[Monitor Model and System  ](./.github/workflows/monitor-pipeline.yml)                  |[![monitoring model and system](https://github.com/konabuta/mlops-azureml/actions/workflows/monitor-pipeline.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/monitor-pipeline.yml)|Run model & system monitoring pipeline.|
|           |[Retraining model and deployment](./.github/workflows/cd-upgrade.yml)                  |[![outer-loop continuous deployment for model upgrade](https://github.com/konabuta/mlops-azureml/actions/workflows/cd-upgrade.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/cd-upgrade.yml)|Run retraining model pipeline.|

### Task

|Stages     |Task                                        |Status          |Description     |
|-----------|--------------------------------------------|----------------|----------------|
|Inner Loop |[Initial model development](./inner-loop/experimental_model_training/)                   |[![train-local](https://github.com/konabuta/mlops-azureml/actions/workflows/train-local.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/train-local.yml)|Run first experimental and interactive model training using JupyterNotebook.|
|           |[Training model with MLflow logging](./inner-loop/experimental_model_training/)          |[![train-logging-local](https://github.com/konabuta/mlops-azureml/actions/workflows/train-logging-local.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/train-logging-local.yml)|Log metrics and parameters using MLflow logging|
|           |[Debug trained model](./inner-loop/debug_trained_model/)                         |                |Debug model using `Error Analysis` and `Interpretability` on trained model and create `Responsible AI dashboard`.|
|           |[Training model](./inner-loop/model_training/)                              |[![model-training](https://github.com/konabuta/mlops-azureml/actions/workflows/model-training.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/model-training.yml)|Train model on Compute Clusters.|
|Middle Loop|[Assets](./middle-loop/model_training_with_azureml_assets/)         |[![assets](https://github.com/konabuta/mlops-azureml/actions/workflows/assets.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/assets.yml)|Create Azure ML assets like `Data`, `Environment` and `Compute`.|
|           |[Model Registry](./middle-loop/model_registry/)                              |[![register-model](https://github.com/konabuta/mlops-azureml/actions/workflows/register-model.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/register-model.yml)|Register model as MLflow type.|
|           |[Debug trained model](./middle-loop/debug_trained_model_with_azureml/)                         |                |Debug model using `Error Analysis` and `Interpretability` on trained model and shared `Responsible AI dashboard`.|
|           |[Model Testing](./middle-loop/model_testing/)                               |[![model-testing](https://github.com/konabuta/mlops-azureml/actions/workflows/model-testing.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/model-testing.yml)|Test code by Unit test and code formatting.|
|           |[Pipeline for model training](./middle-loop/model_training_pipeline/)                 |                |Build pipeline for reproducible training job.|
|Outer Loop |[Model deployment into Stage](./outer-loop/model_deployment_into_stage/)                 |[![model-deployment-into-stage-blue](https://github.com/konabuta/mlops-azureml/actions/workflows/model-deployment-into-stage-blue.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/model-deployment-into-stage-blue.yml)|Deploy first model into Stage Endpoint.|
|           |[Endpoints testing](./outer-loop/endpoints_testing/)                           |[![endpoints-testing](https://github.com/konabuta/mlops-azureml/actions/workflows/endpoints-testing.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/endpoints-testing.yml)|Test Stage Endpoint using sample data.|
|           |[Promote into Prod ](./outer-loop/model_deployment_into_prod/)                          |[![model-deployment-into-prod-blue](https://github.com/konabuta/mlops-azureml/actions/workflows/model-deployment-into-prod-blue.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/model-deployment-into-prod-blue.yml)|Deploy first model into Prod Endpoint.|
|           |[Monitoring Model and System](./outer-loop/monitoring_model_and_system/)                 |                |Monitor Model performance and system performance and detect data drift.|
|           |[Retraining model](./outer-loop/retraining_model/)                            |                |Retrain model using new data.|
|           |[Compare against challenger model](./outer-loop/compare_against_challenger_model/)            |                |Check if new trained model performs better.|
|           |[Model deployment into existing Endpoints  ](./outer-loop/model_deployment_into_existing_endpoints/)  |[![model-deployment-into-existing-endpoints](https://github.com/konabuta/mlops-azureml/actions/workflows/model_deployment_into_existing_endpoints.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/model_deployment_into_existing_endpoints.yml)|Deploy new trained model into existing Stage & Prod Endpoints.|
|           |[Safe roll out](./outer-loop/safe_roll_out/)                               |[![safe-rollout](https://github.com/konabuta/mlops-azureml/actions/workflows/safe-rollout.yml/badge.svg)](https://github.com/konabuta/mlops-azureml/actions/workflows/safe-rollout.yml)|Allocate some traffic into new deployed model.|

*Click link in Task column to see the codes and configurations.
*Almost every task is evaluated using GitHub Actions


## Acknowledgements

This repo is created mainly by FastTrack for Azure team and Cloud Solution Architect team : Keita Onabuta, Meer Alam, Shunta Ito, Kohei Ogawa.
We also build on top of many great codes and packages listed [ACKNOWLEDGEMENTS.md](./ACKNOWLEDGEMENTS.md). Please check them out!


## Reference