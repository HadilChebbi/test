# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:25:12 2020

@author: hadil
"""

import numpy as np
import pandas as pd
import torch
import seaborn as sns
import matplotlib.pyplot as plt


#importing the data set

def read_data(file_path):
    df=pd.read_csv(file_path, sep=',')
    return df

#read_data("sales_train.csv") 
#make sure that the file is in the same repository as the file code so that the instruction below works

