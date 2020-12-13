from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents =  file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup)
# print(soup.prettify())

print(soup.a)

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)


print(tag.get("href"))

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.text)
print(section_heading.get("class"))

company_url = soup.select_one(selector="#name")
print(company_url)

para = soup.find_all("p")
for item in para:
    print(item.text)