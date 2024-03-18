# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
from bs4 import BeautifulSoup
import sys

def get_weather(city):
    url = f"https://yandex.ru/pogoda/{city}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        weather_data = {}

        # Парсим температуру
        temperature_element = soup.find("span", class_="temp__value")
        if temperature_element:
            temperature = temperature_element.text
        else:
            temperature = "Нет данных"
        weather_data["Температура"] = temperature

        # Парсим влажность
        humidity_element = soup.find("div", class_="term term_orient_v fact__humidity")
        if humidity_element:
            humidity = humidity_element.find("div", class_="term__value").text.strip()
        else:
            humidity = "Нет данных"
        weather_data["Влажность"] = humidity

        # Парсим давление
        pressure_element = soup.find("div", class_="term term_orient_v fact__pressure")
        if pressure_element:
            pressure = pressure_element.find("div", class_="term__value").text.strip()
        else:
            pressure = "Нет данных"
        weather_data["Давление"] = pressure

        # Парсим ветер
        wind_element = soup.find("div", class_="term term_orient_v fact__wind-speed")
        if wind_element:
            wind = wind_element.find("div", class_="term__value").text.strip()
        else:
            wind = "Нет данных"
        weather_data["Ветер"] = wind

        return weather_data
    else:
        print("Не удалось получить данные о погоде")
        return None



def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <город>")
        return

    city = sys.argv[1]
    weather = get_weather(city)

    if weather:
        print(f"Погода в городе {city}:")
        for param in sys.argv[2:]:
            if param in weather:
                print(f"{param}: {weather[param]}")
            else:
                print(f"Данные о параметре {param} отсутствуют или не найдены")

if __name__ == "__main__":
    main()
