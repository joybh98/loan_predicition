import os 
import json 
import numpy as np
import pandas as pd
import dill as pickle
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import make_pipeline

import warnings
warnings.filterwarnings("ignore")

# Build the model and train 
def build_and_train():
    data = pd.read_csv('train.csv')
    #use dropna to fill NaN values as it can create problem when training the model
    data = data.dropna(subset=['Gender','Married','Credit_History','LoanAmount']) 
    pred_var = ['Gender','Married','Dependents','Education']