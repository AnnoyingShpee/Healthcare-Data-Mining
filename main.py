import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


train_data_file = "data/disease_train.csv"
test_data_file = "data/disease_test.csv"
prediction_data_file = "data/predictedTarget.csv"


def split_to_train_val(data: pd.DataFrame, split_value=0.3, random=None):

    return


def main():
    train_data = pd.read_csv(train_data_file, delimiter=",")
    test_data = pd.read_csv(test_data_file, delimiter=",")


if __name__ == '__main__':
    main()

