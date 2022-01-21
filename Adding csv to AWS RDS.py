#!pip install PyMySQL
import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine
# credentials to access aws database
username='#'
password='#'
host='#'
database='#'
# read the csv file
df=pd.read_csv('my_crypto_investments.csv')
df['Date']=pd.to_datetime(df['Date'], format='%d-%m-%Y')
# establish a database connection
conn=pymysql.connect(user=username,password=password,host=host,database=database)
cursor=conn.cursor()

def insert_data(table_name,df,username=username,password=password,host=host,database=database,conn=conn,cursor=cursor):
    # changing python datatypes to sql datatypes
    dtypes_sql={
    'object':'varchar',
    'int64':'int',
    'float64':'float',
    'datetime64[ns]':'date',
    'timedelta64[ns]':'varchar'
    }
    col_str=", ".join("{} {}({})".format(n,d,50) if d=='varchar' else "{} {}".format(n,d) for n,d in zip(df.columns,df.dtypes.replace(dtypes_sql)))
    # create a table if it doesn't exist
    cursor.execute("drop table if exists %s;" %(table_name))
    cursor.execute("create table %s(%s)" %(table_name,col_str))
    cursor.connection.commit()
    # copy the csv file to the database
    engine = create_engine("mysql+pymysql://{user}:{pw}@crypto.cfeucnwsd8ed.us-east-1.rds.amazonaws.com/{db}"
                           .format(user=username, pw=password, db=database))
    df.to_sql('{}'.format(table_name), con = engine, if_exists = 'append', chunksize = 1000,index=False)
    # return statement to check if the table is inserted properly
    return pd.read_sql('select * from %s' %(table_name),con=conn)

# define the table name and call the insert_data to insert a csv file into the database
tbl='crypto_inv'
insert_data('{}'.format(tbl),df)
