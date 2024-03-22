import numpy as np
import pandas as pd
import math as m


train_data_file = "data/disease_train.csv"
test_data_file = "data/disease_test.csv"
pred_data_file = "data/predictedTarget.csv"


def read_csv_file(file_name: str, delimiter=','):
    """
    Reads a CSV file and returns the data as a DataFrame
    :param file_name: Name of file
    :param delimiter: Separator between columns
    :return:
    """
    data_frame = pd.read_csv(file_name, delimiter=delimiter)
    return data_frame


def main():
    train_data = read_csv_file(train_data_file)
    test_data = read_csv_file(test_data_file)


if __name__ == '__main__':
    main()

