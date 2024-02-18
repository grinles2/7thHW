import requests
import lxml
from bs4 import BeautifulSoup

url = "https://cash-backer.club/shops" #Сайт
header = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"}    #Сессия
session = requests.session()

for j in range(1, 10):
    print(f"PAGE = {j}")
    with open("grosseries.txt", "a", encoding="UTF-8") as file:
        file.write(f"{j}\n")
    url = f"https://cash-backer.club/shops?page={j}/"  #Страница магазига

    response = session.get(url, headers=header)
    # 200-300 ок 300-400 перенаправление 400-500 страница не найдена и 500-600 сервер проблем
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        allProduct = soup.find("div", class_="row col-lg-9 col-md-9 col-12")   # где твоары
        # print(allProduct)
        products = allProduct.find_all("div", class_="product-info") #все товары
        for i in range(len(products)):
            try:
                title = products[i].find("a", class_="shop-title").text.strip() # товар и имя
                cashback = products[i].find("span", class_="shop_rate").text.strip() # Строчка с кешбеком
                print(title, cashback)
                with open("grocceries.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} --->>> {cashback}\n")
            except:
                print(title, cashback)
