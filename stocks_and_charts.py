import pandas as pd
import time
import requests
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
import numpy as np 
from pandas.plotting import register_matplotlib_converters
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
from finance_num_formatting import format_financial_number

#print(time.ctime())
register_matplotlib_converters()
default_time_value = 3
current_stock = yf.Ticker("MSFT")
stock_info_dict = current_stock.info
stock_short_name = stock_info_dict.get("shortName")
chart_timeframes = ['1-Day', '1-Month', '6-Month', '1-Year', '5-Year', 'Max Length']
current_timeframe = chart_timeframes[default_time_value]
chart_periods = ['1d','1mo','6mo','1y','5y','max']
current_period = chart_periods[default_time_value]
#print(time.ctime())

#print(msft_monthly_prices.iat[row_length-1,3])




def set_current_stock(stock_ticker_string):
    global current_stock
    global stock_info_dict
    global stock_short_name
    current_stock = yf.Ticker(stock_ticker_string)
    stock_info_dict = current_stock.info
    stock_short_name = stock_info_dict.get("shortName")
    build_chart()

def get_current_stock():
    return current_stock

def get_stock_info_dict():
    return stock_info_dict


def set_current_timeframe(timeframe):
    global current_timeframe
    current_timeframe = timeframe

def set_current_period(period):
    global current_period
    current_period = period

def get_stock_name(tickerSymbol):
    current_stock = yf.Ticker(tickerSymbol)
    stock_info_dict = current_stock.info
    stock_short_name = stock_info_dict.get("shortName")
    return stock_short_name




# Use this function to get the live price when a previous and recent call has not already been made for a dataframe with the daily or monthly price data
# If such a dataframe has already been loaded, simply access the latest price in that DF 
# We do this to prevent unnecessary calls to the Yahoo API which slow us down
# A function for finding the current/most recent price from an already loaded dataframe is below this function
def get_live_price_first(stock_ticker):
    temp_price_df = stock_ticker.history(period= '1d', interval = '5m')
    return temp_price_df.iat[0,3]


#Use this function to get the live price when you have recently loaded a dataframe with price history via the ____.history() call
#Useful for situations where the cost of making an API call is not justified by any new data
#May configure future logic to swap between these two functions if market is open (9-4 M-F) or closed, will depend on how often the API is queried by the finished app
def get_live_price(stock_price_dataframe):
    dummy_DF = pd.DataFrame()
    if type(stock_price_dataframe) == type(dummy_DF) and stock_price_dataframe.columns[3] == "Close":
        return stock_price_dataframe.iat[len(stock_price_dataframe)-1,3]
    else:
        return "Error: Argument passed not a valid dataframe containing Closing price data in the third column"
    


current_price_dataframe = pd.DataFrame()

def request_price_dataframe(stock_ticker):
    global current_price_dataframe
    if current_period == '1d':
         current_price_dataframe = stock_ticker.history(period= current_period, interval = '15m')
    elif current_period == '5y':
        current_price_dataframe = stock_ticker.history(period= current_period, interval = '1wk')
    elif current_period == 'max':
        current_price_dataframe = stock_ticker.history(period= current_period, interval = '1mo')
    else:   
        current_price_dataframe = stock_ticker.history(period= current_period)

def get_closing_price_list(stock_ticker):
    closing_prices = current_price_dataframe["Close"]
    return closing_prices

def get_date_list(stock_ticker):
    closing_prices = current_price_dataframe["Close"]
    date_array = closing_prices.index.values
    return date_array

financials = current_stock.financials

#print(financials)


def get_index():
    list_index = []
    for i in financials.index:
        list_index.append(i)
    return list_index

#print(get_index())

def get_column_one_data():
    final_data = []
    data = []
    for i in range(len(financials)):
        x = financials.iloc[i, 0]
        data.append(x)
    for j in data:
        if j is None:
            #print(j)
            final_data.append(j)
        else:
            if j < 0:
                positive = abs(j)
                y = format_financial_number(positive)
                full_string = " - " + y
                #print(full_string)
                final_data.append(full_string)
            else:
                z = format_financial_number(j)
                final_data.append(z)
    return final_data

#print(get_column_one_data())



def get_column_two_data():
    final_data = []
    data = []
    for i in range(len(financials)):
        x = financials.iloc[i, 1]
        data.append(x)
    for j in data:
        if j is None:
            #print(j)
            final_data.append(j)
        else:
            if j < 0:
                positive = abs(j)
                y = format_financial_number(positive)
                full_string = " - " + y
                #print(full_string)
                final_data.append(full_string)
            else:
                z = format_financial_number(j)
                final_data.append(z)
    return final_data

#print(get_column_two_data())


def get_column_three_data():
    final_data = []
    data = []
    for i in range(len(financials)):
        x = financials.iloc[i, 2]
        data.append(x)
    for j in data:
        if j is None:
            #print(j)
            final_data.append(j)
        else:
            if j < 0:
                positive = abs(j)
                y = format_financial_number(positive)
                full_string = " - " + y
                #print(full_string)
                final_data.append(full_string)
            else:
                z = format_financial_number(j)
                final_data.append(z)
    return final_data

#print(get_column_three_data())


def get_column_four_data():
    final_data = []
    data = []
    for i in range(len(financials)):
        x = financials.iloc[i, 3]
        data.append(x)
    for j in data:
        if j is None:
            #print(j)
            final_data.append(j)
        else:
            if j < 0:
                positive = abs(j)
                y = format_financial_number(positive)
                full_string = " - " + y
                #print(full_string)
                final_data.append(full_string)
            else:
                z = format_financial_number(j)
                final_data.append(z)
    return final_data

#print(get_column_four_data())



# modified_financial_data = (pd.DataFrame.from_items([
#     ("Breakdown", get_index()),
#     ("2019-06-30", get_column_one_data()),
#     ("2018-06-30", get_column_two_data()),
#     ("2017-06-30", get_column_three_data()),
#     ("2016-06-30", get_column_four_data())
# ]))

# modified_financial_data = (pd.DataFrame.from_items([
#     ("Breakdown", ['Research Development', 'Effect Of Accounting Charges', 'Income Before Tax', 'Minority Interest', 'Net Income', 'Selling General Administrative', 'Gross Profit', 'Ebit', 'Operating Income', 'Other Operating Expenses', 'Interest Expense', 'Extraordinary Items', 'Non Recurring', 'Other Items', 'Income Tax Expense', 'Total Revenue', 'Total Operating Expenses', 'Cost Of Revenue', 'Total Other Income Expense Net', 'Discontinued Operations', 'Net Income From Continuing Ops', 'Net Income Applicable To Common Shares']),
#     ("2019-06-30", ['16.8 Trillion', None, '43.6 Trillion', None, '39.2 Trillion', '23.0 Trillion', '82.9 Trillion', '42.9 Trillion', '42.9 Trillion', None, ' - 2.6 Billion', None, None, None, '4.4 Billion', '125.8 Trillion', '82.8 Trillion', '42.9 Trillion', '729.0 Billion', None, '39.2 Trillion', '39.2 Trillion']),
#     ("2018-06-30", ['14.7 Trillion', None, '36.4 Trillion', None, '16.5 Trillion', '22.2 Trillion', '72.0 Trillion', '35.0 Trillion', '35.0 Trillion', None, ' - 2.7 Billion', None, None, None, '19.9 Trillion', '110.3 Trillion', '75.3 Trillion', '38.3 Trillion', '1.4 Billion', None, '16.5 Trillion', '16.5 Trillion']),
#     ("2017-06-30", ['13.0 Trillion', None, '29.9 Trillion', None, '25.4 Trillion', '19.9 Trillion', '62.3 Trillion', '29.3 Trillion', '29.3 Trillion', None, ' - 2.2 Billion', None, None, None, '4.4 Billion', '96.5 Trillion', '67.2 Trillion', '34.2 Trillion', '570.0 Billion', None, '25.4 Trillion', '25.4 Trillion']),
#     ("2016-06-30", ['11.9 Trillion', None, '25.6 Trillion', None, '20.5 Trillion', '19.1 Trillion', '58.3 Trillion', '27.1 Trillion', '27.1 Trillion', None, ' - 1.2 Billion', None, None, None, '5.1 Billion', '91.1 Trillion', '63.9 Trillion', '32.7 Trillion', ' - 1.5 Billion', None, '20.5 Trillion', '20.5 Trillion'])
# ]))

#print("Financials for", current_stock.ticker)
#print(modified_financial_data)


# import imgkit
# import pandas
# import os
# import pdfkit
# import codecs
# import io
# data = modified_financial_data

# config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe")

# css = """
# <style type=\"text/css\">
# body {
#     width: 1000px;
# }
# table {
# color: #333;
# font-family: Arial;
# width: 100%;
# border-collapse:
# collapse; 
# border-spacing: 0;
# }
# td, th {
# border: 1px solid transparent; /* No more visible border */
# height: 35px;
# }
# th {
# background: #DFDFDF; /* Darken header a bit */
# font-weight: bold;
# }
# td {
# background: #FAFAFA;
# text-align: center;
# }
# table tr:nth-child(odd) td{
# background-color: white;
# }
# </style>
# """

# def DataFrame_to_image(data, css, outputfile, format):

#     fn = "filename.html"

#     try:
#         os.remove(fn)
#     except:
#         None

#     text_file = open(fn, "a", encoding="ansi", errors="ignore")

#     # # write the CSS
#     text_file.write(css)
#     # # write the HTML-ized Pandas DataFrame
#     text_file.write(data.to_html())
#     text_file.close()
#     #with codecs.open(fn, 'a', encoding='utf-8') as f:
#     #     f.write(data.to_html())
#     # # text_file = codecs.open(fn, "a", "utf-8")
#     # # text_file.write(u'\ufeff')
#     # f.close()

#     # file = open(fn, 'a', encoding='utf8', errors="ignore")
#     # file.write(data.to_html())
#         # f.write(data.to_html())
#     # text_file = codecs.open(fn, "a", "utf-8")
#     # text_file.write(u'\ufeff')
#     # file.close()

#     # page = urllib.request.urlopen('http://homepage.mac.com/s_lott/books/index.html')
#     # text = page.read().decode("utf8")
#     # print(text)

#     pdfkit.from_file(fn, 'financial_data.png', configuration = config)


# DataFrame_to_image(data, css, "financial_data.png", "png")



def build_chart():
    request_price_dataframe(current_stock)
    price_list = get_closing_price_list(current_stock)
    date_list = get_date_list(current_stock)
    build_chart_image(date_list, price_list)


#plt.tick_params(pad = 30)
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.yticks(np.arange(price_list.min(), price_list.max(), step= 10 ))


def build_chart_image(date_list, price_list):
    plt.clf()
    plt.rcParams["figure.figsize"] = [10, 4.8]
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'xkcd:light grey'
    plt_text_color = 'black'
    plt.rcParams['text.color'] = plt_text_color
    plt.rcParams['axes.labelcolor'] = plt_text_color
    plt.rcParams['xtick.color'] = plt_text_color
    plt.rcParams['ytick.color'] = plt_text_color
    plt.rcParams['axes.formatter.useoffset'] = False
    #plt.yscale('log')
    plt.plot(date_list, price_list)
    plt.title(stock_short_name + ' ' + current_timeframe + ' Price Chart')
    plt.savefig("current_chart.png", bbox_inches = 'tight')
    #plt.show()



#build_chart()
#print(time.ctime())



#calling the following two lines will show you the error message caused by the yFinance headers bug
#There is a potential fix available on the issues tab of the YFinance github's issue page
#After this push, will attempt to integrate this hotfix and begin testing for any errors

#test_stock = yf.Ticker("SPCE")
#stock_info_dict = test_stock.info.get("shortName")
