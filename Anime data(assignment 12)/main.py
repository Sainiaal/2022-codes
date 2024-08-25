import requests
from bs4 import BeautifulSoup

# ----------------------------------------- web scraping -----------------------------------------

URL = "https://www.imdb.com/search/title/?at=0&genres=animation&keywords=anime&num_votes=1000,&sort=user_rating&title_type=tv_series"

response = requests.get(url=URL)
soup = BeautifulSoup(response.content, "html.parser")
anime = soup.find_all("div", "lister-item-content")
a_list = []
for i in range(0, len(anime)):
    number = anime[i].find("span", "lister-item-index").get_text().split(".")[0]
    title = anime[i].find("a").get_text()
    year = anime[i].find("span", "lister-item-year").get_text()
    genre = anime[i].find("span", "genre").get_text().split("\n")[1]
    clean_genre = genre.split("            ")[0]
    rating = anime[i].find("strong").get_text()
    votes = anime[i].find("p", "sort-num_votes-visible").find_all("span")[1].get_text()

    try:
        runtime = anime[i].find("span", "runtime").get_text()
    except AttributeError:
        runtime = ""
    a_dict = {"ranking": int(number),
              "name": title,
              "year": year,
              "runtime": runtime,
              "genre": clean_genre,
              "rating": rating,
              "votes": votes}
    a_list.append(a_dict)

# ----------------------------------------- Sheety -----------------------------------------

sheety_api = "https://api.sheety.co/f27e16300ff05eda97d46a5e5dcc7768/anime/sheet1"

for value in a_list:
    data_json = {"sheet1": value}
    response = requests.post(url=sheety_api, json=data_json)
    print(response)
