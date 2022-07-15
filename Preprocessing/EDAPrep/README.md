### Preprocessing and Visualization: 

#### Import packages:
``` python 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
![](https://i.imgur.com/waxVImv.png)
#### Read data:
``` python
data = pd.read_csv('data.csv')
```
![](https://i.imgur.com/waxVImv.png)
#### Missing Values (remove row):
``` python 
data['column'].isnull().sum()

data.dropna(inplace=True)
```
![](https://i.imgur.com/waxVImv.png)
#### Categorical to Numerical:
``` python 
df[['data']] = df[['data']]. apply(pd.to_numeric, errors='coerce')
```
![](https://i.imgur.com/waxVImv.png)
#### Correlation:

``` python
df_corr = df.corr() # method: pearson
```
![](https://i.imgur.com/waxVImv.png)
#### Visualization:
*Example:*
+ ``` python
  plt.figure(figsize=(20, 12))
  sns.heatmap(data, cmap='YlGnBu', annot=True)
  ```
+ ``` python
  sns.pairplot(data)
  ```
+ ``` python
  sns.jointplot(data['column name'], data['column name'])
  ```
+ ``` python
  sns.distplot(data['column name'])
  ```
+ ``` python
  sns.stripplot(data['column name'], data['column name'])
  ```
+ ``` python
  sns.regplot(data=data, x='column name', y='column name')
  ```
+ ``` python
  sns.swarmplot(data['column name'], data['column name'])
  ```
+ ``` python
  sns.boxplot(data['column name'], data['column name'], hue=data['column name'])
  ```
+ ``` python 
  sns.barplot(data['column name'], data['column name'], hue=data['column name'])
  ```
