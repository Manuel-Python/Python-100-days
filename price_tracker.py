from bs4 import BeautifulSoup
import requests

x = requests.get('https://www.amazon.com.au/GoPro-HERO8-Black-Waterproof-Stabilization/dp/B08C7FBW4N/ref=sr_1_12?crid=19VRISJG5EQBI&dchild=1&keywords=action+camera&qid=1608455621&sprefix=action+%2Caps%2C373&sr=8-12',
                 headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:78.0) Gecko/20100101 Firefox/78.0",
                          "Accept-Language": "en-US,en;q=0.5"
                          })

response = x.text
soup = BeautifulSoup(response, "html.parser")
spans = soup.find('span', {'id' : "priceblock_dealprice"})
print(spans.get_text())
#print(response)<span id="priceblock_dealprice" class="a-size-medium a-color-price priceBlockDealPriceString">$386.97</span>