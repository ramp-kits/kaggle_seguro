import numpy as np
import pandas as pd

train_filename = 'data/train.csv'
data = pd.read_csv(train_filename)
size = 500
mock_data = data.iloc[:500]
for column in mock_data.columns:
    mock_data[column] = np.random.choice(data[column], size, replace=False)
mock_data_train = mock_data.iloc[:400]
mock_data_test = mock_data.iloc[400:]
mock_data_sample_submission = mock_data_test[['id', 'target']]
mock_data_test = mock_data_test.drop('target', axis=1)
mock_data_train.to_csv('mock_data/train.csv')
mock_data_test.to_csv('mock_data/test.csv')
mock_data_sample_submission.to_csv('mock_data/sample_submission.csv')
