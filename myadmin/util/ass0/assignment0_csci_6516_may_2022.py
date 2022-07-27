import numpy as np
import requests
import io
import numpy as np 
from numpy import log,dot,e,shape
import matplotlib.pyplot as plt

import torch
import torch.nn.functional as f

%matplotlib inline
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim

# Create linearly separable data
x,y = make_blobs(n_samples=1000, n_features=2, centers=[[-4,-2],[4,2]], cluster_std=1, shuffle=True)
print("X is:")
print(x)
print("y is:")
print(y)
print(shape(x))
print(shape(y))
colors = np.array(['red','green'])
plt.scatter(x[:, 0], x[:, 1],
            color = colors[y].tolist(), marker='.')
xmin, xmax = xlim()