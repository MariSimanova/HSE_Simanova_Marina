
import requests
from bs4 import BeautifulSoup

class ParserCBRF:
    def __init__(self):
        self.url = "https://www.cbr.ru/hd_base/KeyRate/"
        self.data = {}

    def __fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Ошибка загрузки страницы: {e}")
            return None

    def __parse_data(self, html):
        if not html:
            return

        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', class_='data')
        if not table:
            print("Таблица не найдена")
            return

        rows = table.find_all('tr')[1:]
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                date = cols[0].text.strip()
                rate = cols[1].text.strip().replace(',', '.')
                try:
                    self.data[date] = float(rate)
                except ValueError:
                    print(f"Ошибка преобразования ставки для даты {date}: {rate}")

    def start(self):
        html = self.__fetch_page()
        self.__parse_data(html)
        return self.data

# Пример
if __name__ == "__main__":
    parser = ParserCBRF()
    rates = parser.start()
    if rates:
        print("Ключевые ставки ЦБ РФ:")
        for date, rate in list(rates.items())[:5]:
            print(f"Дата: {date}, Ставка: {rate}%")