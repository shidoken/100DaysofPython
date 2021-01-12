from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_article = response.text
soup = BeautifulSoup(yc_article, "html.parser")

print(soup.title.text)

links = soup.select(".athing .storylink")
article_texts = []
article_links = []
for link in links:
    text = link.text
    article_texts.append(text)
    linkage = link.get("href")
    article_links.append(linkage)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)


max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)

print(article_texts[max_index])
print(article_links[max_index])


# with open("website.html", "r") as site:
#     content = site.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.li)
# print(soup.p)
# print(soup.findAll('a'))
# print(soup.findAll('p'))
# for tag in soup.findAll('p'):
#     print(tag.getText())

# for tag in soup.findAll('a'):
#     print(tag.get("href"))

# heading = soup.find("h1", id="name")
# print(heading)

# section_heading = soup.find("h3", class_="heading")
# print(section_heading.text)

# company_url = soup.select_one("p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)