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

feature_table = pd.read_csv('feature_count_table.csv', sep = '\t') # count table - with absolute counts
feature_table = feature_table.transpose() # transpose so that samples are rows
sample_table = pd.read_csv('metadata.txt', sep='\t') # metadata file that has information about samples - cancer vs non cancer, tissue site, control vs experimental, etc.
pca = PCA(n_components=2) # two components to keep for graphing
principalComponents = pca.fit_transform(np.array(feature_table)) 
plot_df = pd.DataFrame(data = principalComponents, columns = ['dim1', 'dim2'], index = feature_table.index)
# We can then plot this like so:
sns.scatterplot(x = 'dim1', y = 'dim2', data = plot_df)

# plot_df = pd.concat([plot_df, sample_table['env_feature']], axis = 1)

# color the dots by a variable from the sample_table
plot_df['envfeature'] = list(sample_table['histology_cat']) # make sure the sample names match
sns.scatterplot(x = 'dim1', y = 'dim2', hue = 'env_feature', data = plot_df)

# run tsne with the bray-curtis distance metric, default perplexity (less than number of samples and between 5 and 50), and default square_distances
tsne = TSNE(metric = 'braycurtis', perplexity=30.0, square_distances=True)
embeddings = tsne.fit_transform(feature_table)
# run pca on the tsne fit feature_table
principalComponentsembed = pca.fit_transform(np.array(embeddings))
plot_df = pd.DataFrame(data = principalComponentsembed, columns = ['dim1', 'dim2'], index = feature_table.index)

plot_df['envfeature'] = list(sample_table['histology_cat']) # make sure the sample names match
sns.scatterplot(x = 'dim1', y = 'dim2', hue = 'envfeature', data = plot_df) # color by the envfeature variable




