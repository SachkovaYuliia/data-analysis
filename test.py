# Напишіть ваш код нижче та натисніть Shift+Enter для виконання
from google.colab import files
import pandas as pd

uploaded = files.upload()

for fn in uploaded.keys():
    print(f'User uploaded file "{fn}" with length {len(uploaded[fn])} bytes')

DATA_PATH = 'clean_data2.csv'

df = pd.read_csv(DATA_PATH, sep=',', encoding='cp1252')

print(df.head())
