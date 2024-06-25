import pandas as pd
import numpy as np
import os


def read_data(dir_path: str, aggregate_min: int = 60):
    """
    Read each dataset from folder and aggregate all time series to common sampling frequency assuming all of
    them have same sampling frequency
    :param dir_path: Folder which contains all dataset files with common sampling frequency
    :param aggregate_min: The level of aggregation of all time series. Default - 60 minutes (1 hour)
    :return: Single dataframe combining all the time series into sample sampling frequency
    """
    files_list = [os.path.join(dir_path, f) for f in os.listdir(dir_path)]

    # Read all frames as stack them horizontally to create one common data panel
    panel = pd.read_csv(files_list[0], index_col="date", parse_dates=True)
    for i in range(1, len(files_list)):
        data = pd.read_csv(files_list[i], index_col="date", parse_dates=True)
        panel = pd.merge(panel, data, how="inner", left_index=True, right_index=True)
