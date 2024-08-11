import sklearn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
# K - means
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# Gaussian mixture model
from sklearn.mixture import GaussianMixture
# Dimensionality reduction
from sklearn.decomposition import PCA


# function for quick scatter plot
def plot_scatter(df,x_column,y_column,title="Scatter Plot",xlabel=None,ylabel=None):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column], alpha=0.5)
    plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Creates full path for dataset_name.csv
headers = ['date','time','user','status']
path = os.path.join(os.getcwd(),'logins.txt')
df = pd.read_csv(path , sep='\t', names=headers)

# Read in dataset
X = pd.read_csv(path)


pca = PCA(n_components=2)
x_reduced = pca.fit_transform(X)


