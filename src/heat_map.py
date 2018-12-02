import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

def draw(matrix):
    ax = sns.heatmap(matrix,  cmap="coolwarm")
    plt.show()