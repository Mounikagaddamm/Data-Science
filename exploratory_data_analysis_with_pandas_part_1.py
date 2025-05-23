# -*- coding: utf-8 -*-
"""Exploratory Data Analysis With Pandas : Part-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-48oRW-Xx48nr5b8q8CnkZZzaEcbMY_2

## Exploratory Data Analysis With Pandas : Part-1

# Data Loading
"""

import numpy as np
import pandas as pd

data = pd.read_csv('/Marks.csv')
df = pd.DataFrame(data)
print(df)

"""# Basic Data Inspection"""

df.head()

df.tail()

df.dtypes

df.describe()

df.info()

"""# Data Cleaning"""

df.isnull().sum()

df.fillna(100)

df.dropna()

df.rename(columns={'Customer_Gender' : 'CGender'})

df.drop(columns=['Transaction_ID'])

"""# Data Transformation"""

df['Stock'].apply(lambda x: x*2)

df.groupby('Product_ID').agg({'Category':'sum'})

df.pivot_table(index='Brand',values='Price',aggfunc='mean')

"""# Data Visualization Integration"""

df['Discount'].hist()

df.boxplot(column=['Price','Discount'])

df.plot.scatter(x='Price',y='Discount')

df.plot.line()

df['Stock'].value_counts().plot.bar()

"""# Statistical Analysis"""

df=df.select_dtypes(include='number')
df.corr()

df.cov()

df['Profit'].value_counts()

df['Stock'].unique()

df['Discount'].nunique()

"""# Indexing And Selection"""

df['Final_Price']

df[['Profit','Price']]

df.iloc[0:5]

df[df['Discount']>19]

"""# Data Formating And Conversion"""

df['Profit'].astype('int')

df.set_index('Profit')

"""# Advanced Data Transformation"""

df.apply(lambda x : x+1)

df.melt(id_vars=['Profit'])

df.stack(),df.unstack()

pd.crosstab(df['Price'],df['Profit'])



