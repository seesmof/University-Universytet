import os
import pandas as pd
from sklearn.model_selection import train_test_split

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, 'train.csv')
df = pd.read_csv(file_path)
needed='Survived,Name,Age'.split(',')
df=df[needed].dropna()
print(df)
