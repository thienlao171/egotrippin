import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today=datetime.today().strftime("%d/%m/%Y")
load={'date_req':today}
response=requests.get(url, params=load)
xml=BeautifulSoup(response.content, 'html.parser') #html.parser

def getCourse(id):
    return xml.find('valute', {'id':id}).value.text