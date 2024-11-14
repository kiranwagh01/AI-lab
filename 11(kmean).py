import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Read the dataset using pandas.read_csv(dataset.csv)

sales = pd.read_csv("/data/Programming/AI LAb/sales_data_sample.csv", sep=",", encoding='Latin-1')

sales.head()

sales.info()

# Take only two columns PRICEEACH and SALES

sales = sales[['PRICEEACH', 'SALES']]


sales.head()

wcss = []

for i in range(1, 11):
    print(i)
    km = KMeans(n_clusters=i)
    km.fit(sales)
    wcss.append(km.inertia_)

wcss

plt.plot(range(1, 11), wcss, label='Number of clusters vs WCSS')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.legend()

km = KMeans(n_clusters=3)

km_pred = km.fit_predict(sales)

plt.scatter(sales[km_pred == 0]['PRICEEACH'], sales[km_pred == 0]['SALES'], label='Cluster 1')
plt.scatter(sales[km_pred == 1]['PRICEEACH'], sales[km_pred == 1]['SALES'], label='Cluster 2')
plt.scatter(sales[km_pred == 2]['PRICEEACH'], sales[km_pred == 2]['SALES'], label='Cluster 3')
plt.xlabel('PRICE')
plt.ylabel('SALES')
plt.legend()


