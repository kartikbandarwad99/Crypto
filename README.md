# Crypto Price Forecasting
Building an End to End ML Project
## Scrapping Crypto Prices data from Yahoo Finance
Refer to [crypto scraping](https://github.com/kartikbandarwad99/Crypto/blob/main/Crypto_scrapping.py) file for scrapping using Yahoo Financials library
Install the following libraries to use scrape data from yahoo finance:
```python
!pip install yahoofinancials
 !pip install yfinance
 ```
 Historical prices of a cryptocurrency(in INR, to get the prices in USD change to USD) till present date can be scraped using get_history function and passing the abrevation into function
   * Upload the csv files to aws database
      So that data gets updated from time to time
      
