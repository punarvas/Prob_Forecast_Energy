import config
import os
from utils import data_utils

if __name__ == "__main__":
    dirs = os.listdir(config.DATASET_BASE_PATH)
    print(f"Found directories: {dirs}")

    data_utils.read_data(os.path.join(config.DATASET_BASE_PATH, dirs[0]), aggregate_min=10)
