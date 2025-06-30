import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('fivethirtyeight')

data = sns.load_dataset('tips')

data.head()

sns.relplot(x='total_bill', y='tip', data=data)
sns.

sns.relplot(x='total_bill', y='tip', hue='smoker', data=data)

sns.relplot(x='total_bill', y='tip', hue='smoker', style='sex', data=data)

sns.relplot(x='total_bill', y='tip', hue='smoker', style='sex', size='size', data=data)

sns.scatterplot(x='total_bill', y='tip', hue='smoker', style='sex', data=data)

# x axis  categorical data
# y axis numerical data

sns.catplot(x='day', y='tip', data = data)

sns.catplot(x='day', y='tip', jitter=0, data = data)

sns.catplot(x='day', y='tip', jitter=10, data = data)

sns.catplot(x='day', y='tip', kind='box', data = data)

sns.catplot(x='day', y='tip', kind='boxen', data = data)

sns.catplot(x='day', y='tip', kind='violin', data = data)

sns.catplot(x='day', y='tip', kind='bar', data = data)

sns.catplot(x='day', y='tip', kind='swarm', data = data)

sns.catplot(x='day', y='tip', kind='swarm', hue='sex', data = data)

sns.swarmplot(x='day', y='tip', data = data)

sns.boxplot(
    data['tip']
)

sns.boxplot(data['total_bill'])

sns.catplot(x='day', y='total_bill', kind='box', data=data)

sns.catplot(x='day', y='total_bill', kind='box', hue='sex', data=data)

sns.violinplot(data['total_bill'])

sns.catplot(x='day', y='total_bill', kind='violin', data=data)

sns.catplot(x='day', y='total_bill', kind='violin', hue='sex', data=data)

sns.catplot(x='day', y='total_bill', kind='violin', hue='sex', split=True, data=data)

sns.jointplot(x='total_bill', y='tip', data=data)

sns.jointplot(x='total_bill', y='tip', kind='reg', data=data)

sns.jointplot(x='total_bill', y='tip', kind='reg', truncate=False, data=data)

