import requests
from bs4 import BeautifulSoup

url = "https://www.shadowfox.in/domains"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Status Code:", response.status_code)

print("\nPAGE TITLE:")
print(soup.title.get_text(strip=True))

print("\nHEADINGS:")

headings = soup.find_all(["h1", "h2", "h3"])

for heading in headings:
    print(heading.get_text(" ", strip=True))