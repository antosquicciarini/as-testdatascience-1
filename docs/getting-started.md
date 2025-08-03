# Getting Started

This guide will help you set up and run the AS-TestDataScience-1 project locally.

## 🧰 Requirements

- Python 3.8 or later  
- Git  
- `make` (for UNIX systems) or Git Bash if using Windows  
- One of:  
  - [Conda](https://docs.conda.io/en/latest/miniconda.html) (recommended)  
  - Virtualenv / venv

## 🔄 Clone the Repository

    git clone https://github.com/antosquicciarini/as-testdatascience-1.git
    cd as-testdatascience-1

## 🧪 Create and Activate Environment

If you have Conda:

    make create_environment
    conda activate as-testdatascience-1

If using virtualenv instead:

    python3 -m venv .venv
    source .venv/bin/activate
    make requirements

## 📦 Install Dependencies

    make requirements

This will install all necessary Python packages from `requirements.txt`.

## ✅ Test the Environment

Check that Python version and packages are set up correctly:

    make test_environment

Expected output:

    >>> Development environment passes all tests!

## 🚀 Run the Notebook

Launch Jupyter and run the main notebook:

    jupyter notebook

Then open and execute:

    notebooks/covertype.ipynb

## 🧹 Clean Temporary Files (Optional)

    make clean

Removes all compiled Python files and `__pycache__` folders.

## 📦 Extra Utilities

You can also sync data with AWS S3 if configured:

    make sync_data_to_s3
    make sync_data_from_s3

Or check code style:

    make lint