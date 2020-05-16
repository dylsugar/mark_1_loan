# Importing some important librarys

import pandas as pd
-
import os
import warnings
warnings.filterwarnings('ignore')

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv(r'C:\Users\dylan\PycharmProjects\mark_1_loan\loan.csv')
print(df.shape)

loan_col = df.columns
print("Loan Columns")
print(loan_col)
df.head()
df.info()
