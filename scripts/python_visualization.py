#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sidra
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

feature_table = pd.read_csv('feature_count_table.csv', sep = '\t') # count table
feature_table = feature_table.transpose() # transpose so that samples are rows
sample_table = pd.read_csv('metadata.txt', sep='\t') # metadata file that has information about samples - cancer vs non cancer, tissue site, control vs experimental, etc.
pca = PCA(n_components=2) # two components to keep for graphing
principalComponents = pca.fit_transform(np.array(feature_table)) 
plot_df = pd.DataFrame(data = principalComponents, columns = ['dim1', 'dim2'], index = feature_table.index)
# We can then plot this like so:
sns.scatterplot(x = 'dim1', y = 'dim2', data = plot_df)

plot_df = pd.concat([plot_df, sample_table['env_feature']], axis = 1)
sns.scatterplot(x = 'dim1', y = 'dim2', hue = 'env_feature', data = plot_df)
