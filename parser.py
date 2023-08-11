import requests
from bs4 import BeautifulSoup
import csv
import re

#url = "https://twitter.com/search?q=icebucket&src=typed_query&f=live"
url = "https://www.fotor.com/ru/"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# with open("data/index.html", "w", encoding="UTF-8") as file:
#      file.write(src)

with open("data/index.html", encoding="UTF-8") as file:
    src = file.read()


    soup = BeautifulSoup(src, "lxml")
    count = 0
    lst = [[], [], [], [], [], []]
    get_headers = soup.find_all("nav", class_='Footer_footerNav__adqqs')
    for item in get_headers:
        if count < 100:
            get_names_h3 = item.find("h3")
            if get_names_h3:
                print(get_names_h3.text, end='\n\n')
                lst[count].append(get_names_h3.text)

                get_names_reg = item.find('div', class_='Footer_footerNav__hide__16BaK').find_all('div', class_='Footer_footerNav__linkWrap__15BBL')
                for item_2 in get_names_reg:

                    get_links = item_2.find("a")
                    x = f'{get_links.text}: {get_links.get("href")}'
                    lst[count].append(get_links.text)
                    if get_names_reg.index(item_2) == (len(get_names_reg)-1):
                        print(x, end='\n\n')
                    else:
                        print(x)

        if count != len(lst) - 1:
            count += 1

    print(lst)

    for i in lst:
        with open('data/list.csv', 'a', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(

                    i,

            )

    # get_names = soup.find_all("div", class_='Footer_footerNav')
    # for item in get_headers:
    #     get_names_2 = item.find_all("div", class_='Footer_footerNav')
    #     for item_2 in get_names_2:
    #         get_names_3 = item_2.find("a")
    #         print(get_names_3)
