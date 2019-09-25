import requests
import smtplib
import time
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal

# testing git

URL = input("Please give me the link of the card you are after: ")
test_value = input("How much are you willing to pay? ")
recipient = input("Please give me the email address you want to be notified: ")

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
sold_out_flag = True
out_stock_flag = False

def check_price():
    price = soup.find_all('span', class_='money')[0].get_text()
    global value
    value = Decimal(sub(r'[^\d.]', '', price))
    user_value = Decimal(sub(r'[^\d.]', '', test_value))

    if (user_value > value):
        send_mail(out_stock_flag)
        print('E-mail successfully sent!')
    
    
def send_mail(out_stock_flag):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # establishes a connection
    server.starttls() # starts our encryption
    server.ehlo()
    
    server.login('richard23496@gmail.com', 'fhjwlddkipfkfosb')
    subject ='Important email!'

    if (out_stock_flag == False):
        body = 'Hi! The item you are after is below the price you wanted to pay. The URL of the item is {} and the price of the card is ${}'.format(URL, value)
    elif (out_stock_flag == True):
        body = 'Hi! The item you are after is currently out of stock.'
    
    msg = f"Subject: {subject}\n\n{body}" # f = format string

    server.sendmail(
        'richard23496@gmail.com', recipient, msg
    )
    
    server.quit()

    # mail has been sent so we good
    global price_mail
    price_mail = True
    

price_mail = False

# this section tests if the stock is sold out or not, assume it is out of stock, unless proven otherwise
while (sold_out_flag):
    try:
        # testing to see if the item is out of stock or not
        stock = soup.find_all('span', class_='productlabel soldout')[0].get_text()
        if stock in 'Sold Out':
            out_stock_flag = True

        if(price_mail == False):
            check_price()
        
    except:
        # if the item is in stock, it will come here
        sold_out_flag = False
        print('The item is in stock')

        # at this point mail has not been sent yet

        price_mail = False
        
        while(price_mail == False):
            check_price()
            print('I am checking the price')
