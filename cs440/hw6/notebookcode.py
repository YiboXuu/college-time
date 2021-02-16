#!/usr/bin/env python
# coding: utf-8

# $\newcommand{\xv}{\mathbf{x}}
# \newcommand{\Xv}{\mathbf{X}}
# \newcommand{\yv}{\mathbf{y}}
# \newcommand{\zv}{\mathbf{z}}
# \newcommand{\av}{\mathbf{a}}
# \newcommand{\Wv}{\mathbf{W}}
# \newcommand{\wv}{\mathbf{w}}
# \newcommand{\tv}{\mathbf{t}}
# \newcommand{\Tv}{\mathbf{T}}
# \newcommand{\muv}{\boldsymbol{\mu}}
# \newcommand{\sigmav}{\boldsymbol{\sigma}}
# \newcommand{\phiv}{\boldsymbol{\phi}}
# \newcommand{\Phiv}{\boldsymbol{\Phi}}
# \newcommand{\Sigmav}{\boldsymbol{\Sigma}}
# \newcommand{\Lambdav}{\boldsymbol{\Lambda}}
# \newcommand{\half}{\frac{1}{2}}
# \newcommand{\argmax}[1]{\underset{#1}{\operatorname{argmax}}}
# \newcommand{\argmin}[1]{\underset{#1}{\operatorname{argmin}}}$

# # Assignment 6: Neural Networks

# Yibo Xu
# 

# ## Overview

# You will write and apply code that trains neural networks of various numbers of hidden layers and units in each hidden layer and returns results as specified below.  You will do this once for a regression problem and once for a classification problem. 

# ## Required Code

# Define the following two functions to train neural networks using `pytorch` and the `Adam` optimizer, one for a regression problem and one for a classification problem:
# 
# * `nnet, error_trace = train_for_regression(X, T, hidden_layers, n_epochs, learning_rate)`
# 
# Given
# 
#    * `X`: `np.array` of shape `n_samples` X `n_inputs` of input samples,
#    * `T`: `np.array` of shape `n_samples` X `n_outputs` of desired values for each sample,
#    * `hidden_layers`: list of integers of number of units in each hidden layer.  The length of this list is the number of hidden layers.
#    * `n_epochs`: number of epochs to train for,
#    * `learning_rate`: the learning rate used for the Adam optimizer function.
#     
# Return
# 
#    * `nnet`: the trained neural network model
#    * `error_trace`: list of RMSE value for each epoch
#    
# * `nnet, error_trace = train_for_classification(X, T, hidden_layers, n_epochs, learning_rate)`
# 
# Given values that are the same as  ones for `train_for_regression` except for
# 
#    * `T`: `np.array` of shape `n_samples` X 1 of correct class labels for each sample, and must be integers from $\{0, 1, \ldots, K-1\}$ where $K$ is the number of classes,
#    * `error_trace`: list of likelihood value for each epoch

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import torch
import pandas as pd
import os


# In[3]:




def train_for_regression(X, T, hidden_layers, n_epochs, learning_rate):

    Xt = torch.from_numpy(X).float()
    Tt = torch.from_numpy(T).float()
    
    n_inputs = X.shape[1]
    n_outputs = T.shape[1]
   
    layer_objects  = [torch.nn.Linear(n_inputs, hidden_layers[0]), torch.nn.Tanh()]
    
    if(len(hidden_layers) > 1):
        for loop1 in range (len(hidden_layers) - 1):
            layer_objects.append(torch.nn.Linear(hidden_layers[loop1], hidden_layers[loop1 + 1]))
            layer_objects.append(torch.nn.Tanh())
    layer_objects.append(torch.nn.Linear(hidden_layers[len(hidden_layers) - 1], n_outputs))
    layer_objects.append(torch.nn.Tanh())
    
    if(hidden_layers == []):
         layer_objects = [torch.nn.Linear(n_inputs, []), torch.nn.Tanh(),
                          torch.nn.Linear([], n_outputs)]
    
    nnet = torch.nn.Sequential(*layer_objects)                           
    
    mse_f = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(nnet.parameters(), lr=learning_rate)
    learning_curve = []

    for epoch in range(n_epochs):
    
        Y = nnet(Xt)
        mse = mse_f(Y, Tt)  
        
        optimizer.zero_grad()
        mse.backward()
        optimizer.step()  
        
        if epoch == n_epochs-1:
            learning_curve.append(mse.detach().sqrt().item())
        
       # print(TrainData) 
       # learning_curve.append(TrainData)
       
    return nnet, learning_curve


# In[4]:


X = (np.arange(10) - 5).reshape(-1, 1)
T = np.sin(X)
nnet, error_trace = train_for_regression(X, T, [20], 2000, 0.01)


# In[5]:


def forward_all_layers2(nnet, X, learning_curve, nll):
    Ys = [X]
    for layer in nnet:
        learning_curve.append((-nll.detach()).exp().item())
    return learning_curve

def train_for_classification(X, T, hidden_layers, n_epochs, learning_rate):

    n_classes = len(np.unique(T))

    n_inputs = X.shape[1]
    n_outputs = len(np.unique(T))

    Xt = torch.from_numpy(X).float()
    Tt = torch.from_numpy(T).reshape(-1).long()
    
    
    layer_object = []
    for i in range(len(hidden_layers)):
        layer_object.append(torch.nn.Linear(n_inputs, hidden_layers[i]))
        layer_object.append(torch.nn.Tanh())
        if i == len(hidden_layers)-1:
            layer_object.append((torch.nn.Linear(hidden_layers[i], n_outputs)))
                  
    nnet = torch.nn.Sequential(*layer_object)                            
    
    
    optimizer = torch.optim.SGD(nnet.parameters(), lr=learning_rate)
    nll_f = torch.nn.NLLLoss()
    learning_curve = []

    
    for epoch in range(n_epochs):
        
        Yt = nnet(Xt)

        nll = nll_f(Yt, Tt)
        
        optimizer.zero_grad()
        nll.backward()
        optimizer.step()
        
        if  epoch == n_epochs-1:
            n_hidden_layers = (len(nnet) - 1) //2
            nplots = 2 + n_hidden_layers


            order = np.argsort(X, axis=0).reshape(-1)
        
            Ys = forward_all_layers2(nnet,X,learning_curve,nll)
          
    
    return nnet, learning_curve


# In[6]:


X = np.linspace(-10, 10, 100).reshape(2, -1).T
T = (np.sin(0.1 * np.abs(X[:,0]) * X[:, 1]) > 0.7).astype(int)
nnet, error_trace = train_for_classification(X, T, [20], 2000, 0.01)


# The following `forward` function may be useful in both of the above functions.

# In[7]:


def forward(nnet, Xt):
    
    Ys = [Xt]
    for layer in nnet:
        Ys.append(layer(Ys[-1]))
        
    return Ys[-1] 


# The function `use` will be used below to apply a `nnet` to input data `X`.

# In[8]:


def use(nnet, X):
    
    Xt = torch.from_numpy(X).float()
    Yt = forward(nnet, Xt)   # nnet(Xt)
    Y = Yt.detach().numpy()
    
    return Y


# The following functions will also be useful.  The first will calculate the accuracy in terms of RMSE of predictions from a neural network applied to a regression problem. The second calculates the accuracy in terms of percent of samples correctly classified by a neural network applied to a classification problem.

# In[9]:


# for regression problem
def rmse(a, b):
    return np.sqrt(np.mean((a - b)**2))

# for classification problem
def percent_correct(a, b):
    return 100 * np.mean(a == b)

def confusion_matrix(Y_classes, T):
    class_names = np.unique(T)
    table = []
    for true_class in class_names:
        row = []
        for Y_class in class_names:
            row.append(100 * np.mean(Y_classes[T == true_class] == Y_class))
        table.append(row)
    conf_matrix = pd.DataFrame(table, index=class_names, columns=class_names)
    conf_matrix.style.background_gradient(cmap='Blues').format("{:.1f}")
    print(f'Percent Correct is {percent_correct(Y_classes, T)}')
    return conf_matrix


# # Regression Problem:  "Turn off the stove!"
# 
# Apply your `train_for_regression` function to the following data.  Read about the data at [here at the UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction#).

# In[10]:


if os.path.isfile('energy.csv'):
    print('Reading data from \'energy.csv\'.')
    energy = pd.read_csv('energy.csv')
else:
    print('Downloading energydata_complete.csv from UCI ML Repository.')
    energy = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00374/energydata_complete.csv')
    print(f'Number rows in original data file {len(energy)}.')
    energy = energy.dropna(axis=0)
    print(f'Number rows after dropping rows with missing values {len(energy)}.')
    energy.to_csv('energy.csv', index=False)  # so row numbers are not written
    print(f'Data saved to \'energy.csv\'')


# In[11]:


energy


# In[12]:


energy.describe()


# In[13]:


energy.values


# In[14]:


X = energy.values[:, 3:-2].astype(np.double)
T = energy.values[:, 1:3].astype(np.double)
X[0]


# In[15]:


Xnames = energy.iloc[:, 3:-2].columns.values.tolist()
Tnames = energy.iloc[:, 1:3].columns.values.tolist()
Xnames, Tnames


# Randomly partition the data into 80% for training and 20% for testing, using the following code cells.

# In[16]:


n_train = int(X.shape[0] * 0.8)
n_train


# In[1]:


# randomly shuffle samples
rows = np.arange(X.shape[0])
np.random.shuffle(rows)
rows


# In[18]:


Xtrain = X[rows[:n_train], :]
Ttrain = T[rows[:n_train], :]

Xtest = X[rows[n_train:], :]
Ttest = T[rows[n_train:], :]

Xmean = Xtrain.mean(axis=0)
Xstd = Xtrain.std(axis=0)

Xtrain = (Xtrain - Xmean) / Xstd
Xtest = (Xtest - Xmean) / Xstd

Xtrain.shape, Ttrain.shape, Xtest.shape, Ttest.shape


# Use at least four calls to `train_for_regression` for four different hidden-layer structures. Include `[]` to test a linear model without hidden layers.  For each one, use 1,000 epochs and a learning rate of 0.01. Plot the resulting `error_trace` for each result.
# 
# For each trained network, call `rmse` to provide the RMSE for the trained network applied to the training data, and again for the testing data.  Create and show a `pandas.DataFrame` that combines these results. **Discuss the values in the table and how they relate to the hidden layer structures. Use at least five sentences.**  Here is an example of what your `DataFrame` should look like.  The RMSE values given are not real results. Your RMSE values may have more digits of precision.

# In[19]:


nnet, error_tracing = train_for_regression(Xtrain,Ttrain,[10],1000,0.01)
Ytrain = use(nnet, Xtrain)
rms1 = rmse(Ytrain,Ttrain)
#print(rmsetest)
Ytest = use(nnet,Xtest)
rms2 = rmse(Ytest,Ttest)
print(rms1)
print(rms2)

nnet, error_tracing3 = train_for_regression(Xtrain,Ttrain,[10],1000,0.01)
Ytrain = use(nnet, Xtrain)
rms3 = rmse(Ytrain,Ttrain)
#print(rmsetest)
Ytest = use(nnet,Xtest)
rms4 = rmse(Ytest,Ttest)
print(rms3)
print(rms4)


nnet, error_tracing5 = train_for_regression(Xtrain,Ttrain,[100],1000,0.01)
Ytrain = use(nnet, Xtrain)
rms5 = rmse(Ytrain,Ttrain)
#print(rmsetest)
Ytest = use(nnet,Xtest)
rms6 = rmse(Ytest,Ttest)
print(rms5)
print(rms6)


nnet, error_tracing7 = train_for_regression(Xtrain,Ttrain,[100,50,50],1000,0.01)
Ytrain = use(nnet, Xtrain)
rms7 = rmse(Ytrain,Ttrain)
#print(rmsetest)
Ytest = use(nnet,Xtest)
rms8 = rmse(Ytest,Ttest)
print(rms7)
print(rms8)




#pd.DataFrame([[[], 12.3, 14.4], [[10], 11.2, 52.2], [[100], 8.2, 22.2], [[100, 50, 50], 65.2, 42.1]],
            #columns=('Hidden Layers', 'RMSE Train', 'RMSE Test'))


# In[20]:


pd.DataFrame([[[],rms1 , rms2], [[10], rms3, rms4], [[100], rms5, rms6], [[100, 50, 50],rms7, rms8]],
            columns=('Hidden Layers', 'RMSE Train', 'RMSE Test'))


# # Disscuion about my result
# 
# 
# Looking at my result, the Rmse of Train are reducing from the 0 to 2 as the hidden layers increasing. That conform to  the nerual networking as machine learned more that will reduce the RMSE. Looking  at the RMSE Test, there is a same thing, the rmse reducing when hidden layers increaing. However,the RMSE from train or test both increased after the hidden layer changed from [100] to [100, 50,50]. That conform to the rule becuse we have more levels of hiden layers.
# 

# In[21]:


pd.DataFrame([[[], 12.3, 14.4], [[10], 11.2, 52.2], [[100], 8.2, 22.2], [[100, 50, 50], 65.2, 42.1]],
            columns=('Hidden Layers', 'RMSE Train', 'RMSE Test'))


# # Classification Problem:  "Is that a frog I hear?"
# 
# Apply your `train_for_classification` function to the following data.  Read about the data at [here at the UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Anuran+Calls+%28MFCCs%29).

# In[22]:


import requests, zipfile, io

if os.path.isfile('frogs.csv'):
    print('Reading data from \'frogs.csv\'.')
    frogs = pd.read_csv('frogs.csv')
else:
    print('Downloading \'Anuran Calls (MFccs).zip\' from UCI ML Repository.')
    r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/00406/Anuran Calls (MFCCs).zip')
    z = zipfile.ZipFile(io.BytesIO(r.content))  # StringIO(r.content))
    frogs = pd.read_csv(z.open('Frogs_MFCCs.csv'))  # read('Frogs_MFCCs.csv'))
    print(f'Number rows in original data file {len(frogs)}.')
    frogs = frogs.dropna(axis=0)
    print(f'Number rows after dropping rows with missing values {len(frogs)}.')
    frogs.to_csv('frogs.csv', index=False)  # so row numbers are not written to 
    print(f'Data saved to \'frogs.csv\'')


# In[23]:


frogs


# We want to classify each sample according to the species of the frog or toad.  So, we must convert the species names to integers from 0 to be our class labels for each sample.  The following code cells do this.

# In[24]:


frogs['Species']


# In[25]:


species = frogs['Species'].values.reshape(-1, 1)
class_names = np.unique(species)
class_names


# In[26]:


species == class_names


# In[27]:


_, column_indices = np.where(species == class_names)
column_indices


# In[ ]:


plt.plot(column_indices)
plt.ylabel('Species (from 0 to 9)')
plt.xlabel('Sample Index');


# Now we can create our data matrices.  Each sample has inputs of the 22 MFCC features, from columns 0 through 21, and the target class labels are the `column_indices`.

# In[37]:


X = frogs.iloc[:, range(22)].values
T = column_indices.reshape(-1, 1)  # to make T a column matrix

Xnames = frogs.iloc[:, range(22)].columns.values
Tnames = ['Species']

X.shape, T.shape


# Use random partitions of the data of 60% for training and 40% for testing.

# In[38]:


n_train = int(X.shape[0] * 0.6)

# randomly shuffle samples
rows = np.arange(X.shape[0])
np.random.shuffle(rows)
Xtrain = X[rows[:n_train], :]
Ttrain = T[rows[:n_train], :]
Xtest = X[rows[n_train:], :]
Ttest = T[rows[n_train:], :]

Xmean = Xtrain.mean(axis=0)
Xstd = Xtrain.std(axis=0)

Xtrain = (Xtrain - Xmean) / Xstd
Xtest = (Xtest - Xmean) / Xstd

Xtrain.shape, Ttrain.shape, Xtest.shape, Ttest.shape


# In[39]:


len(np.unique(Ttrain)), len(np.unique(Ttest))


# Rerun the above two code cells until you get 10 unique values in `Ttrain` and `Ttest`.

# Use at least four calls to `train_for_classification` for four different hidden-layer structures. Include `[]` to test a linear model without hidden layers.  For each one, use 1,000 epochs and a learning rate of 0.01.  Plot the resulting `error_trace` for each result.
# 
# For each trained network, call `percent_correct` to provide the accuracy for the trained network applied to the training data, and again for the testing data.  Create and show a `pandas.DataFrame` that combines these results. **Discuss the values in the table and how they relate to the hidden layer structures. Use at least five sentences.** 
# 
# For the neural network that has the best accuracy on testing data, display the confusion matrix for the network applied to training data and to testing data.  **Discuss the values you see in both confusion matrices with at least five sentences.**

# ## Grading
# 
# Download [A6grader.tar](http://www.cs.colostate.edu/~anderson/cs440/notebooks/A6grader.tar) and extract `A6grader.py` from it.

# In[122]:


get_ipython().run_line_magic('run', '-i "A6grader.py"')


# ## Check-in

# Do not include this section in your notebook.
# 
# Name your notebook ```Lastname-A6.ipynb```.  So, for me it would be ```Anderson-A6.ipynb```.  Submit the file using the ```Assignment 6``` link on [Canvas](https://colostate.instructure.com/courses/109411).

# ## Extra Credit (up to 2 total points)
# 
# Earn 1 point of extra credit by applying `train_for_regression` to a second regression data set from the UCI ML  Repository.
# 
# Earn 1 point of extra credit by applying `train_for_classification` to a second classification data set from the UCI ML Repository.
# 
