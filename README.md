# Scrapping Crypto Prices data from Yahoo Finance
Install the following libraries to use scrape data from yahoo finance:
```python
!pip install yahoofinancials
!pip install yfinance
 ```
 The functions get_history and get_current_data are defined in [Crypto Scrapping](https://github.com/kartikbandarwad99/Crypto/blob/main/Crypto_scrapping.py)
- Historical prices of a cryptocurrency(in INR, to get the prices in USD change to USD) till present date can be scraped using get_history function and passing the abrevation into   function. To get weekly or monthly data change the time interval to weekly or monthly.
  For example:
  ```
  # getting the historical price data for Bitcoin 
  get_history('BTC')
  ```
- To get the current data of the cryptocurrencies(market cap,price,moving average and the traded volume) get_current_data function is defined. A list of abbrevations of required cryptocurrencies needs to be passed to the function
  For example:
  ```
  # getting the current data pass a list of abrevations of cryptocurrencies
  l=['BTC','ETH','SOL','MANA','BAT','SAND','DOGE']
  get_current_data(l)
  ```
 
## Upload the files into AWS cloud database
To setup AWS database and connect to the database using python you can refer [this video](https://www.youtube.com/watch?v=RerDL93sBdY)</br>
The table can be inserted into the specified database using the insert_data function from the [Adding csv to AWS RDS](https://github.com/kartikbandarwad99/Crypto/blob/main/Adding%20csv%20to%20AWS%20RDS.py)
For example:
```python
# For inserting a dataframe df into database with tablename crypto
insert_data('crypto',df,username, password, database_name, host name))
```
The function takes in tablename, dataframe and the user credentials to connect to the AWS database.
