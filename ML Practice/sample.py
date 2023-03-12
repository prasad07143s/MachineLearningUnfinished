# Importing the necessary modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, svm, ensemble, naive_bayes, datasets

# Collecting the data

data = datasets.load_boston()
print(dir(data))
print(data.DESCR)