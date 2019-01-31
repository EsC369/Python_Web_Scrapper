'''
SIMPLE WEBSCRAPPER TO SCRAPE THE PRICE OF ALL BOOKS ON SAID URL And writes them/saves to a cvs file to be viwed in a spreadsheet.
SIMPLY CHANGE THE ELEMENTS AND VARIABLES TO REVERSE ENGINEER THIS TO WORK AS YOU SEE FIT.
'''
from flask import Flask, render_template, request, requests
from bs4 import BeautifulSoup
from csv import writer

# Desired website:
response = requests.get('http://books.toscrape.com/')

# Declare Beautiful Soup Parser:
soup = BeautifulSoup(response.text, 'html.parser')

#Declare Prices variavle:
prices = soup.find_all(class_="product_price")   # find all classes with the name product_price

# Save Data to CVS file:
with open('NameOfFile.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    # headers = ['Title', 'Price']
    headers = ["header1", "header2"]
    csv_writer.writerow(headers)

    # loop through prices content and pinpick desired section/content, then save to CVS file
    for price in prices:
        myPrice = price.get_text().replace('\n', '')[:7]
        csv_writer.writerow([myPrice])   # writes a row of each data into cvs file