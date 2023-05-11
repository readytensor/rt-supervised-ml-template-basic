## Cookiecutter Template for Supervised Learning Models

This is a cookiecutter template for supervised learning models, specifically meant for production deployment. The template is flexible and can be modified as per the needs of specific projects.

This template is used as part of a tutorial series on adaptable machine learning models. The tutorial series is available on the [Ready Tensor](https://www.readytensor.ai/) website.

This project is influenced by the [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science/tree/master).

## Project Structure

This template creates the following project structure:

```bash
<your_chosen_project_name>/
├── inputs/
│   ├── data/
│   │   ├── testing/
│   │   └── training/
│   └── schema/
├── model/
│   └── artifacts/
├── outputs/
│   ├── hpt_outputs/
│   ├── logs/
│   └── predictions/
├── src/
│   ├── config/
│   ├── data_model/
│   ├── hyperparameter_tuning/
│   ├── prediction/
│   ├── preprocessing/
│   ├── schema/
│   ├── xai/
├── tests/
│   ├── <mirrors `/src` structure ...>
│   ...
│   ...
├── tmp/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

- **`/inputs`**: This directory contains all the input files for your project, including the data and schema files. The data is further divided into testing and training subsets.
- **`/model/artifacts`**: This directory is used to store the model artifacts, such as trained models and their parameters.
- **`/outputs`**: The outputs directory contains all output files, including the prediction results, logs, and hyperparameter tuning outputs.
- **`/src`**: This directory holds the source code for the project. It is further divided into various subdirectories such as `config` for configuration files, `data_model` for data models for input validation, `hyperparameter_tuning` for hyperparameter-tuning (HPT) related files, `prediction` for prediction model scripts, `preprocessing` for data preprocessing scripts, `schema` for schema scripts, and `xai` for explainable AI scripts.
- **`/tests`**: This directory contains all the tests for the project. It mirrors the `src` directory structure for consistency.
- **`/tmp`**: This directory is used for storing temporary files which are not necessary to commit to the repository.
- **`.gitignore`**: This file specifies the files and folders that should be ignored by Git.
- **`LICENSE`**: This file contains the license for the project.
- **`README.md`**: This file contains the documentation for the project, explaining how to set it up and use it.
- **`requirements.txt`**: This file lists the dependencies for the project, making it easier to install all necessary packages.

This project structure is designed to be clear and adaptable, making it suitable for a wide range of machine learning tasks. It's important to remember that this structure is not set in stone and can be adjusted based on the specific needs of your project. For example, you may add a `notebooks` directory in the root of the project to store Jupyter notebooks. You may also add a `docs` directory to store the documentation for the project.

## Requirements

- Python 3.6+
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:

  `pip install cookiecutter`
  or

  ```bash
  conda config --add channels conda-forge
  conda install cookiecutter
  ```

- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: `conda install -c conda-forge cookiecutter`

## Usage

Run the following from the command line:

```bash
cookiecutter -c v1 https://github.com/readytensor/rt-supervised-ml-template-basic
```

## Running tests

```bash
py.test tests
```
