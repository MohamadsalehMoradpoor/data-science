## Preprocessing in data mining
+ **Missing Values**
    + remove row
    + constant
    + Mean/Mode/Median
    + Nearest Neighbors
+ **Categorical to Numerical**
    + Ranking
    + Replacement
    + OHE
+ **Scaling**
    + Max-Normalization
    + MinMax-Normalization
    + Z Score (Standard Scaling)

``` python
# Missing Values (Mean/Mode/Median)
from sklearn.impute import SimpleImputer
si = SimpleImputer(missing_values=np.nan, strategy='mean')
X = si.fit_transform(X[:, 1:])

# Missing Values (K Nearest Neighbors(KNN))
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=3)
data = imputer.fit_transform(data)
```

``` python
# Categorical to Numerical (OHE)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:, 0] = le.fit_transform(X[:, 0])

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer((['column name', OneHotEncoder(), [0]]), remainder='passthrough')
X = ct.fit_transform(X)
```
``` python
# Scaling (Z Score (Standard Scaling
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X = ss.fit_transform(X)

# Scaling (MinMax-Normalization)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
data = scaler.fit_transform(data)

# Scaling (Normalizer)
from sklearn.preprocessing import Normalizer
norm = Normalizer()
data = norm.fit_transform(data)

# Scaling (Binarizer)
from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshld=0.0)
data_b = binarizer.fit_transform(data)
```
