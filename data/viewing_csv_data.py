# This script uses pandas to look at the raw CSV data.
# It can be modified in any which way and it won't affect the rest of the app.

import pandas as pd

df = pd.read_csv('tx_deathrow_full.csv')

df.head()

df.shape 
# row = 553, cols = 18

df.isnull().sum()

df.columns