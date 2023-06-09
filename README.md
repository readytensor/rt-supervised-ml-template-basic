## Cookiecutter Template for Supervised Learning Models

This is a cookiecutter template for supervised learning models, specifically meant for production deployment. The template is flexible and can be modified as per the needs of specific projects.

This template is used as part of a tutorial series on adaptable machine learning models. The tutorial series is available on the [Ready Tensor](https://www.readytensor.ai/) website.

Note that the auto-generated template contains the MIT license. You may change the license as per your needs.

This project is influenced by the [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science/tree/master).

## Project Structure

This template creates the following project structure:

```bash
<your_chosen_project_name>/
├── examples/
├── model_inputs_outputs/
│   ├── inputs/
│   │   ├── data/
│   │   │   ├── testing/
│   │   │   └── training/
│   │   └── schema/
│   ├── model/
│   │   └── artifacts/
│   └── outputs/
│       ├── errors/
│       ├── hpt_outputs/
│       └── predictions/
├── requirements/
│   ├── requirements.txt
│   └── requirements_text.txt
├── src/
│   ├── config/
│   ├── data_models/
│   ├── hyperparameter_tuning/
│   ├── prediction/
│   ├── preprocessing/
│   ├── schema/
│   └── xai/
├── tests/
│   ├── integration_tests/
│   ├── performance_tests/
│   └── unit_tests/
│       ├── <mirrors /src structure>
│       └── ...
├── tmp/
├── .gitignore
├── LICENSE
├── README.md
```

- **`/examples`**: This directory contains all files you want to use as examples. Typically, these would be small data files that can be used as examples for the ML project.
- **`/model_inputs_outputs`**: This directory contains files that are either inputs to, or outputs from, the model. This directory is further divided into:
  - **`/inputs`**: This directory contains all the input files for your project, including the `data` and `schema` files. The `data` is further divided into `testing` and `training` subsets.
  - **`/model/artifacts`**: This directory is used to store the model artifacts, such as trained models and their parameters.
  - **`/outputs`**: The outputs directory contains sub-directories for error logs, and hyperparameter tuning outputs, and prediction results. Note that model artifacts should not be saved in this directory. Instead, they should be saved in the `/model/artifacts` directory.
- **`requirements`**: This directory contains the requirements files. You may create multiple requirements files for different purposes, such as `requirements.txt` for the main code in the `src` directory, `requirements_text.txt` for dependencies required to run tests in the `tests` directory. You may optionally have another requirements file to use for linting and style checks.
- **`/src`**: This directory holds the source code for the project. It is further divided into various subdirectories such as `config` for configuration files, `data_models` for data models for input validation, `hyperparameter_tuning` for hyperparameter-tuning (HPT) related files, `prediction` for prediction model scripts, `preprocessing` for data preprocessing scripts, `schema` for schema handler scripts, and `xai` for explainable AI scripts.
- **`/tests`**: This directory contains all the tests for the project. It contains sub-directories for specific types of tests such as unit tests, integration tests, and performance tests. For unit tests, the directory structure should mirror the `/src` directory structure. For example, if you have a `preprocessing` folder in the `/src` directory, then tests corresponding to the scripts under `src/preprocessing` should be placed in the `/tests/unit_tests/preprocessing` directory.
- **`/tmp`**: This directory is used for storing temporary files which are not necessary to commit to the repository.
- **`.gitignore`**: This file specifies the files and folders that should be ignored by Git.
- **`LICENSE`**: This file contains an MIT license for the project. You can change this to any other license you want.
- **`README.md`**: This file contains the documentation for the project, explaining how to set it up and use it.

This project structure is designed to be clear and adaptable, making it suitable for a wide range of machine learning tasks. It's important to remember that this structure is not set in stone and can be adjusted based on the specific needs of your project. For example, you may add a `notebooks` directory in the root of the project to store Jupyter notebooks. You may also add a `docs` directory to store the documentation for the project. Within the `src` folder, you may add a `feature_selection` folder for feature selection scripts.

## Requirements

- Python 3.6+
- cookiecutter Python package >= 1.4.0: `pip install cookiecutter`

## Usage

Run the following from the command line:

```bash
cookiecutter -c v1 https://github.com/readytensor/rt-supervised-ml-template-basic
```

## Installing development dependencies within project

```bash
pip install -r requirements.txt
```

## Running tests

```bash
pytest
```
