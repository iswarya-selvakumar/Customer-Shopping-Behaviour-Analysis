
# Import necessary libraries
import pandas as pd
import pymysql
import sqlalchemy
from sqlalchemy import create_engine
# Read CSV file
df=pd.read_csv("D:/ISWARYA/Project/data sets/customer_shopping_behavior.csv")
print(df.head(10))        # First 10 rows
print(df.columns)         # Columns names
print(df.info())          # Data info
print(df.describe(include='all'))    # Descriptive stats
print(df.isnull().sum())     # Check missing values
# Fill missing Review Rating by median per category
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print('NULL value',df['Review Rating'].isnull().sum())
# Clean column names
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
# Create Column age group
lable= ['Young Adult','Adult','Middle-age','Senior',]
df['age_group']=pd.qcut(df['age'],4,labels=lable)
print(df[['age','age_group']].head(10))
# Create a column Purchase frequency to days
frequency_mapping = {
      'Fortnightly' :14,
      'Weekly'      : 7,
      'Monthly'     : 30,
      'Quarterly'   : 90,
      'Bi-Weekly'   : 14,
      'Annually'    : 365,
      'Every 3 Months' : 90 }
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))
# Check and drop duplicate/unused columns
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied']== df['promo_code_used']).all())
df=df.drop('promo_code_used',axis=1)
print(df.columns)
# Connect to MySQL
host ='localhost'
user ='root'
password='root'
port = 3306
database='customer_behavior'
# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
# upload dataframe
df.to_sql('customer', con=engine, if_exists='replace', index=False)
print("Upload successful!")


