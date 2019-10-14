# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# while this is true (it is true by default),

url = input("What website do you want to watch: ")
search_string =input('What word are you looking to appear? ')
recipient = input("Please give me the email address you want to be notified: ")

while True:
    # set the url as VentureBeat,

    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")
    
    # if the number of times the word "Google" occurs on the page is less than 1,
    if str(soup).find(search_string) == -1:
        # wait 60 seconds,
        print('The word {} has not appeared on the website yet yet, I will check again in one minute'.format(search_string))
        time.sleep(60)
        # continue with the script,
        continue
        
    # but if the word "Google" occurs any other number of times,
    else:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo() # establishes a connection
        server.starttls() # starts our encryption
        server.ehlo()
        
        server.login('richard23496@gmail.com', 'fhjwlddkipfkfosb')
        subject ='Important email!'

        body = 'The {} cards are up on the website! The URL of the item is {}'.format(search_string, url)
        
        msg = f"Subject: {subject}\n\n{body}" # f = format string

        server.sendmail(
            'richard23496@gmail.com', recipient, msg
        )
        print('Email Sent!')
        server.quit()

        break