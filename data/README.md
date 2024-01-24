# Datasets

## Overview

This directory contains datasets utilized in our real estate industry project. Based on stages in our data processing pipeline, the datasets are organized into distinct sub-directories:

- **landing**: The initial datasets fetched from data sources.
- **raw**: Datasets that have undergone preliminary cleaning and preprocessing.
- **curated**: The final datasets ready for analysis and modeling.

## Descriptions

### raw
The `raw` directory hosts datasets in their original format. These datasets have not been subjected to any processing or cleaning. The complete data has been uploaded to GitHub. All data sources are documented in detail in `summary_notebook.ipynb`.

### landing
Datasets in the `landing` directory have been subjected to basic preprocessing steps such as removing duplicates, handling missing values, and type conversions. They serve as a foundation for further refinement and analysis. On GitHub, `landing` is an empty folder. To populate it, one should follow and execute instructions in the `READNE.md` file for whole project sequentially.

### curated
The `curated` directory contains datasets prepared for analysis and modeling. These datasets have undergone comprehensive cleaning, processing, and transformation to meet the project's requirements. Similar to `landing` on GitHub, it remains empty until the sequences of processes are completed, after which files will be stored.