import requests
import smtplib
import time
import sys
import os
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal

URL = 'https://www.nakijo.com.au/collections/mega-tin-2019-mp19/products/borrelsword-dragon-mp19-en097-ultra-rare-1st-edition'
#URL = 'https://www.nakijo.com.au/collections/mega-tin-2019-mp19/products/jackalope-mp19-en139-prismatic-secret-rare-1st-edition'
#URL = input("Please give me the link of the card you are after: ")
test_value = input("Please tell me the price you want to check for: ")

count = 0

def check_stock():
    try: 
        stock = soup.find_all('span', class_='productlabel soldout')[0].get_text()
    except:
        stock = 'In stock'
        # Input code for stock quantity and low stock
        # Low stock sends a different email so have to configure the email message 
    
    if stock in'Sold Out':
        print(stock)
    elif stock in'In stock':
        check_price(stock)
    
def check_price(stock):
    global count
    global value
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
       
    price = soup.find_all('span', class_='money')[0].get_text()
    print(price)

    value = Decimal(sub(r'[^\d.]', '', price))
    #print(value)
    user_value = Decimal(sub(r'[^\d.]', '', test_value))

    print('{} at {}'.format(stock,price))

    if (user_value >= value) and (count is 0):
        #send_mail()
        print('Checkpoint: 1')
        count = 1
    else:
        print('Checkpoint: 2')
    return value

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()       # Establishes a connection
    server.starttls()   # Starts our encryption
    server.ehlo()
    server.login('sonhoangify@gmail.com', 'uushhdgaouselegl')

    subject ='Automated email!'
    body = 'Hi!\n\nThe item you are after is below the price you wanted to pay.\n\nThe URL of the item is {}.\n\nThe price of the card is ${}'.format(URL, value)
    
    msg = f"Subject: {subject}\n\n{body}" # f = format string
    recipients = ['sonhoangify@gmail.com', 'sthoa1@student.monash.edu']

    server.sendmail(
        'sonhoangify@gmail.com', recipients, msg
    )

    print('Email sent!')

    server.quit()

while True:
    check_stock()
    time.sleep(30)

if __name__ == '__main__':
    check_stock()
    os.execv(__file__, sys.argv)
