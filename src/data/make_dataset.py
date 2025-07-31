# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo


def load_dataset():
    """Fetch and process the UCI Covertype dataset."""
    # Dataset Uploading
    covertype = fetch_ucirepo(id=31)

    # data (as pandas dataframes)
    X = covertype.data.features
    y = covertype.data.targets
    df = pd.concat([X, y], axis=1)

    # Target Column
    target_col = 'Cover_Type'

    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # Step 1: Binary columns (two unique values or known binary prefix)
    binary_cols = [
        col for col in numeric_cols
        if col.startswith('Soil_Type') or col.startswith('Wilderness_Area')
    ]

    # Step 2: Quantitative columns (exclude binary columns and target)
    quantitative_cols = [col for col in numeric_cols
                         if col not in binary_cols and col != target_col]

    return df, target_col, quantitative_cols, binary_cols


@click.command()
@click.argument(
    'input_filepath',
    type=click.Path(exists=True)
)
# Placeholder; not used with UCI dataset
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """Runs data processing scripts to turn
    raw data into cleaned data ready to be analyzed."""
    logger = logging.getLogger(__name__)
    logger.info('Fetching and processing the Covertype dataset...')

    df, target_col, quantitative_cols, binary_cols = load_dataset()

    logger.info(
        f'Dataset loaded with shape: {df.shape}'
    )
    logger.info(
        f'Target column: {target_col}'
    )
    logger.info(
        f'Quantitative columns: {len(quantitative_cols)}'
    )
    logger.info(
        f'Binary columns: {len(binary_cols)}'
    )

    df.to_csv(output_filepath, index=False)
    logger.info(
        f'Dataset saved to {output_filepath}'
    )


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    load_dotenv(find_dotenv())

    main()
