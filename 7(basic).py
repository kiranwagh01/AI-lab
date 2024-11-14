import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load data
file = '/data/Programming/AI LAb/iris.csv'
iris_data = pd.read_csv(file)

# Display initial statistics
print("Initial statistics:")
print(iris_data.describe())

# Copy the data
cp = iris_data.copy()

# Check for missing values
missing_values = iris_data.isnull().sum()
print("Missing values in each column:")
print(missing_values[missing_values > 0])

# Handle missing values (already filled)
cp['sepal_length'].fillna(cp['sepal_length'].mean(), inplace=True)
cp['petal_length'].fillna(cp['petal_length'].mean(), inplace=True)
print("\nFilling missing values:")
print(cp.head())

# Scan for outliers
numerical_cols = iris_data.select_dtypes(include=np.number).columns
for col in numerical_cols:
    Q1 = iris_data[col].quantile(0.25)
    Q3 = iris_data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = iris_data[(iris_data[col] < lower_bound) | (iris_data[col] > upper_bound)]
    if not outliers.empty:
        print(f"Outliers in '{col}':")
        print(outliers[[col]])
        print("\n")

# Apply MinMax scaling to 'sepal_length'
scaler = MinMaxScaler()
scaled_sepal_length = scaler.fit_transform(cp[['sepal_length']])
cp['scaled_sepal_length'] = scaled_sepal_length
print("\nScaled Sepal Length:")
print(cp[['sepal_length', 'scaled_sepal_length']].head())

# Label encode the 'species' column
label_encoder = LabelEncoder()
cp['species_encoded'] = label_encoder.fit_transform(cp['species'])
print("\nLabel Encoded 'Species' Column:")
print(cp[['species', 'species_encoded']].head())
