import requests
from bs4 import BeautifulSoup
import smtplib
import re

URL = 'https://www.amazon.in/HP-15-6-inch-Laptop-Sparkling-15q-ds0009TU/dp/B07DZLCBYJ/ref=sr_1_1_sspa?' \
      'keywords=LAPTOP&qid=1561795131&s=gateway&sr=8-1-spons&psc=1'
headers = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers = headers)

    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    result = re.sub('[\W_]+', '', price)

    converted_price = float(result[0:5])

    if(converted_price < 45000.00):
        send_mail()
    print(converted_price)
    print(title.strip())

    if(converted_price < 45000.00):
        send_mail()
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('call2abhimishra@gmail.com','rcjklioicvykakqt')

    subject = 'price fall down'
    body = 'check the amzon link https://www.amazon.in/HP-15-6-inch-Laptop-Sparkling-15q-ds0009TU/dp/B07DZLCBYJ/ref=sr_1_1_sspa?' \
      'keywords=LAPTOP&qid=1561795131&s=gateway&sr=8-1-spons&psc=1'

    msg = f"subject: {subject}\n\n{body}"
    server.sendmail(
        'call2abhimishra@gmail.com',
        'ab.mishra@yahoo.com',
        msg
    )
    print('hey email is send')

    server.quit()

check_price()