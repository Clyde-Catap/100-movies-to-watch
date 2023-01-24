import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

data = requests.get(f"{URL}")
real_data = data.text


# Write your code below this line 👇
soup = BeautifulSoup(real_data, features="html.parser")
Titles = soup.find_all("h3")

listed_title = []

ascending_order = []


for title in Titles:
    x = title.text
    listed_title.append(x)

for gg in range(1,101):
    w = (listed_title[100-gg])
    ascending_order.append(w)



with open("movies.txt", "w", encoding="utf-8") as file:
    for a in ascending_order:
        file.write(f"{a}\n")

#
