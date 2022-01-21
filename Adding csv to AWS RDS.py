#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install PyMySQL
import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine
os.chdir('D:\\Crypto')


# In[2]:


username='admin'
password='12345678'
host='crypto.cfeucnwsd8ed.us-east-1.rds.amazonaws.com'
database='crypto_price'


# In[10]:


df=pd.read_csv('my_crypto_investments.csv')
df['Date']=pd.to_datetime(df['Date'].astype(str), format='%d-%m-%Y')
df


# In[13]:


conn=pymysql.connect(user=username,password=password,host=host,database='crypto_price')
cursor=conn.cursor()


# In[18]:


def insert_data(table_name,df,username=username,password=password,host=host,database=database,conn=conn,cursor=cursor):
    # changing python datatypes to sql datatypes
    dtypes_sql={
    'object':'varchar',
    'int64':'int',
    'float64':'float',
    'datetime64[ns]':'date',
    'timedelta64[ns]':'varchar'
    }
    col_str=", ".join("{} {}".format(n,d) for n,d in zip(df.columns,df.dtypes.replace(dtypes_sql)))
    # establish connection to database
    #conn=pymysql.connect(user=username,password=password,host=host,database=database)
    #cursor=conn.cursor()
    # creating table and adding records
    col_str=", ".join("{} {}({})".format(n,d,50) if d=='varchar' else "{} {}".format(n,d) for n,d in zip(df.columns,df.dtypes.replace(dtypes_sql)))
    cursor.execute("drop table if exists %s;" %(table_name))
    cursor.execute("create table %s(%s)" %(table_name,col_str))
    cursor.connection.commit()
    engine = create_engine("mysql+pymysql://{user}:{pw}@crypto.cfeucnwsd8ed.us-east-1.rds.amazonaws.com/{db}"
                           .format(user=username, pw=password, db=database))
    df.to_sql('{}'.format(table_name), con = engine, if_exists = 'append', chunksize = 1000,index=False)
    
    return pd.read_sql('select * from %s' %(table_name),con=conn)
    


    
# In[24]:


tbl='crypto_inv'
insert_data('{}'.format(tbl),df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




