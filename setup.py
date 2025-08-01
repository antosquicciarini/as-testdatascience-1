import pandas as pd
from setuptools import find_packages, setup

setup(
    name='as-testdatascience-1',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description='Multiclass classification of forest cover type using the Forest Cover Type dataset (UCI). Includes EDA, preprocessing, model evaluation, and selection based on performance metrics. Fully structured and reproducible project.',
    author='Antonio Squicciarini',
    license='MIT',
)
