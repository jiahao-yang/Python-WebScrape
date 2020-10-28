from bs4 import BeautifulSoup
import requests
import re

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())

name = soup.p.name
print(name)
print(soup.p.attrs)

print(soup.head)

soup.find_all('a')

for tag in soup.find_all(True):
    print(tag.name)

print(soup.find_all('p', 'course'))

print(soup.find_all(id='link1'))

print(soup.find_all(id=re.compile('link')))

print(soup.find_all(string = re.compile('python')))