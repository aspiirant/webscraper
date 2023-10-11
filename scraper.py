import time
import requests
from bs4 import BeautifulSoup
import csv

# url/website die je wilt scrapen
url = "https://www.microsoft.com/nl-nl/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # zoekt alle a tags
    links = soup.find_all("a")
      

    for link in links:
        print(link.get("href"))
        
    # maakt een scraped.csv aan en schrijft alle data erin
    with open('scraped.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Link'])
        for link in links:
            writer.writerow([link.get("href")])
            

    title = soup.title.string
    print("Page Title:", title)
    

    search_word = "" # zoek een woord op de pagina
    word_count = soup.get_text().lower().count(search_word.lower())
    print("Occurrences of '{}' on the page: {}".format(search_word, word_count))
else:
    print("Request failed with status code:", response.status_code)

time.sleep(1.5)
