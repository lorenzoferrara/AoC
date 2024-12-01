import numpy as np
import pandas as pd

import time


t0 = time.time()

df = pd.read_csv('input.txt', sep='   ', header=None, names=['L1', 'L2'], index_col=False)

# print(df)

df['L1'] = np.sort(df['L1'])
df['L2'] = np.sort(df['L2'])

c= sum([np.abs(a-b) for a, b in zip(df['L1'], df['L2'])])


print(c)

##################

total = 0
for i in df['L1']:
    count = df['L2'].where(df['L2']==i, other=0).sum()
    total += count

print(total)

###############

print(f"Execution time: {time.time() - t0}")