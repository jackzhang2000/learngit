def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # 仅权重和偏置与AND不同！
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 仅权重和偏置与AND不同！
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

import numpy as np
x = np.array([-1.0, 1.0, 2.0])
y = x > 0
y = y.astype(np.int)

import numpy as np
import matplotlib.pylab as plt
def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # 指定y轴的范围
plt.show()

def E_y(ys:np.array):
    """
    ys: A batch of column vectors
    return: Mean of the column vectors
    """
    return np.mean(ys, axis=0)


import numpy as np
A = np.sqrt(np.arange(12).reshape(3, 4))   # some 3 by 4 array
b = np.array([[2], [4], [5]])              # some 3 by 1 vector
cov = np.dot(b.T - b.mean(), A - A.mean(axis=0)) / (b.shape[0]-1)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
sigmoid(x)

#1st layer
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
print(W1.shape) # (2, 3)
print(X.shape) # (2,)
print(B1.shape) # (3,)
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
print(Z1.shape) # (3,)
print(W2.shape) # (3, 2)
print(B2.shape) # (2,)
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

#Hidden layer activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Output layer activation function
def identity_function(x):
    return x
#回归问题用恒等函数，分类问题用softmax 函数

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3) # 或者Y = A3

def identity_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y) # [ 0.31682708 0.69627909]

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a) # 指数函数

sum_exp_a = np.sum(exp_a) # 指数函数的和

y = exp_a / sum_exp_a

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

y = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
pred = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
mean_squared_error(np.array(y), np.array(t))

pred = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
cross_entropy_error(np.array(y), np.array(t))

#Cholesky Decomposition
from numpy import array
from numpy.linalg import cholesky# define a 3x3 matrix
A = array([[36, 30, 18], [30, 41, 23], [18, 23, 14]])
print(L)# Cholesky decomposition
L = cholesky(A)
print(L)
print(L.T)# reconstruct
B = L.dot(L.T)
print(B)

https://stats.stackexchange.com/questions/160054/how-to-use-the-cholesky-decomposition-or-an-alternative-for-correlated-data-si
import numpy as np

def E_y(ys:np.array):
    """
    ys: A batch of column vectors
    return: Mean of the column vectors
    """
    return np.mean(ys, axis=0)

def E_yyT(ys:np.array):
    """
    ys: A batch of column vectors
    return: Covariance matrix of the column vectors
    """
    ys_trans = ys.transpose(0, 2, 1)
    return np.mean(ys@ys_trans, axis=0)

A = np.random.randint(low=1,high=10,size=(M,M))
A[np.triu_indices(M,k=1)] = 0
C = A@A.T
mu = np.random.randint(low=0,high=10,size=(1,M,1))
mu
np.diag(mu.ravel())

no_obs = 1000             # Number of observations per column
means = [6, 5, 4, 3, 8]         # Mean values of each column
no_cols = 3               # Number of columns

sds = [6, 5, 4, 3, 8]           # SD of each column
sd = np.diag(sds)         # SD in a diagonal matrix for later operations

observations = np.random.normal(0, 1, (no_cols, no_obs)) # Rd draws N(0,1) in [3 x 1,000]
cor_matrix = np.array([[1.0, 0.6, 0.9],
                       [0.6, 1.0, 0.5],
                       [0.9, 0.5, 1.0]])          # The correlation matrix [3 x 3]

cov_matrix = np.dot(sd, np.dot(cor_matrix, sd))   # The covariance matrix

Chol = np.linalg.cholesky(cov_matrix)             # Cholesky decomposition

sam_eq_mean = Chol.dot(observations)             # Generating random MVN (0, cov_matrix)

s = sam_eq_mean.transpose() + means               # Adding the means column wise
samples = s.transpose()                           # Transposing back

print(np.corrcoef(samples))                       # Checking correlation consistency.

def function_1(x):
    return 0.01*x**2 + 0.1*x

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

import numpy as np
import matplotlib.pylab as plt
x = np.arange(0.0, 20.0, 0.1) # 以0.1为单位，从0到20的数组x
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

numerical_diff(function_1, 5)

def function_2(x):
    return x[0] ** 2 + x[1] ** 2

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

numerical_diff(function_tmp1, 3.0)