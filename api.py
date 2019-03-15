import pandas as pd
import numpy as np
import LoanPrediction

# Import Dataset
dset = pd.read_csv('train.csv')

# Replace NAN Values with 0 

def changeToZero():
    categoricals = []
    for col, col_type in dset_.dtypes.iteritems():
        if col_type == '0':
            categoricals.append(col)
        else:
            dset[col].fillna(0,inplace = True)