import requests                 # imports requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com"      # calls the url inputed and gets the response status requested
response = requests.get(url)

if response.status_code == 200:         # 200 means that its working, 404 means error
    print("success")
else:
    print("failed")

soup = BeautifulSoup(response.text, 'html.parser')      # this line allows to navigate and extract data from the HTML

title = soup.title      # finds the title html element
print('Title:', title.text)

paragraphs = soup.find_all("p")     # i have no idea what im doing
for paragraph in paragraphs:
    print('Paragraph: ', paragraph.text)