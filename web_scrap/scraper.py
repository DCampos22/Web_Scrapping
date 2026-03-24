import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

countries = soup.find_all("div", class_="country")

for country in countries:
    name = country.find("h3", class_="country-name").text.strip()
    capital = country.find("span", class_="country-capital").text.strip()
    population = country.find("span", class_="country-population").text.strip()
    area = country.find("span", class_="country-area").text.strip()

    print(f"{name} | Capital: {capital} | Population: {population} | Area: {area} km²")