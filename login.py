import os
import time
import requests
import lxml
from bs4 import BeautifulSoup
#-------------------------------------------------------------------------
welcome = "Добро Пожаловать на BomjPaket.com"
welcome1 = "Наш сайт помогает вам с экономить на покупках мы показываем самые актуальные скидки в магазинах 60+ магазинов в нашей базе"
print(welcome)
time.sleep(1)
print(welcome1)
time.sleep(2)
#-------------------------------------------------------------------------
print("Привет хотите войти или зарегистрироваться")
ans1 = input(" Войти(1)  Зарегистрироваться(2):")
os.system('cls')
if ans1 == "1":
    login = input(" Введите Логин:")
    password = input(" Введите Пароль:")
    exit(" Аккаунт не найден")
    # -------------------------------------------------------------------------
if ans1 == "2":
    os.system('cls||clear') # очистика консоли но в pycharm она не работает  в Replit она работает
    login = input("Введите ваш никнейм:")
    password = input("Введите ваш пароль:")
    print("Аккаунт не зарегистрирован")
    print("База-Данных не отвечает ваш аккаунт не сохранён,вы можете пользоваться аккаунтом")
    time.sleep(2)
    os.system('cls||clear')
    ans2 = input("Хотите продолжить?")
if ans2 == "y" or "д" or "yes" or "да" or "lf" or "da":
    #Программа
    import requests
    import lxml
    from bs4 import BeautifulSoup

    url = "https://cash-backer.club/shops"  # Сайт
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"}  # Сессия
    session = requests.session()
    for j in range(1, 10):
        # print(f"PAGE = {j}")
        # Зачем следующие 2 строчки кода? что ты пишешь в файл?
        with open("cashback.txt", "a", encoding="UTF-8") as file:
            file.write(f"{j}\n")
        url = f"https://cash-backer.club/shops?page={j}/"  # Страница магазига
        response = session.get(url, headers=header)
        # 200-300 ок 300-400 перенаправление 400-500 страница не найдена и 500-600 сервер проблем
        # print(response)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            allProduct = soup.find("div", class_="row col-lg-9 col-md-9 col-12")  # где твоары
            # print(allProduct)  # Смотрим весь HTML файл сайта

            products = allProduct.find_all("div", class_="product-info")  # все товары
            products = allProduct.find_all("div",
                                           class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")  # все товары
            for i in range(len(products)):
                try:
                    title = products[i].find("div", class_="shop-title").text.strip()  # товар и имя
                    cashback = products[i].find("div", class_="shop-rate").text.strip()  # Строчка с кешбеком
                    print(title, cashback)  # выводим
                    with open("cashback.txt", "a", encoding="UTF-8") as file:
                        file.write(f"{title} --->>> {cashback}\n")
                except:
                    print(title, cashback)
    # Программа
if ans2 == "n" or "no" or "нет" or "н" or "net":
    exit("Выход программы")
else:
    exit("Невозможно выяснить что вы ввели")
# -------------------------------------------------------------------------