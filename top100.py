from bs4 import BeautifulSoup
import requests

x = requests.get('https://www.billboard.com/charts/hot-100/1985-08-12')

response = x.text

soup = BeautifulSoup(response, "html.parser")
spans = soup.find_all('span', {'class' : "chart-element__information__song text--truncate color--primary"})

lines = [span.get_text() for span in spans]
for song in lines:
    print(song)