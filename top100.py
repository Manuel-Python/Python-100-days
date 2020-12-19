from bs4 import BeautifulSoup
import requests

x = requests.get('https://www.billboard.com/charts/hot-100/1984-06-12')

response = x.text

soup = BeautifulSoup(response, "html.parser")
spans = soup.find_all('span', {'class' : "chart-element__information__song text--truncate color--primary"})

lines = [span.get_text() for span in spans]

song_list = {}
index = 1
for song in lines:
    song_list[index] = song
    index += 1


keys = song_list.keys()
print(keys)
for key in keys:
    print(song_list[key])
