import csv
import json


def process_traders_with_info(inn_file: str, info_file: str, output_file: str):

    traders_data = []

    inns = []
    try:
        with open(inn_file, 'r', encoding='utf-8') as f:
            inns = [line.strip() for line in f
                    if line.strip() and line.strip().isdigit()]
        if not inns:
            print(f"Ошибка: файл {inn_file} пустой или не содержит валидных ИНН")
            return
        print(f"Прочитано ИНН из {inn_file}: {inns}")
    except FileNotFoundError:
        print(f"Файл {inn_file} не найден")
        return
    except UnicodeDecodeError:
        print(f"Ошибка: файл {inn_file} не в кодировке UTF-8. Пробуем cp1251.")
        try:
            with open(inn_file, 'r', encoding='cp1251') as f:
                inns = [line.strip() for line in f if line.strip() and line.strip().isdigit()]
            if not inns:
                print(f"Ошибка: файл {inn_file} пустой или не содержит валидных ИНН")
                return
            print(f"Прочитано ИНН из {inn_file}: {inns}")
        except Exception as e:
            print(f"Ошибка при повторной попытке чтения {inn_file}: {e}")
            return

    try:
        with open(info_file, 'r', encoding='utf-8') as f:
            org_data = json.load(f)

        for inn in inns:
            found = False
            for org in org_data:
                if org.get('inn') == inn:
                    traders_data.append([inn, org.get('ogrn', ''), org.get('address', '')])
                    print(f"Найдено для ИНН={inn}: ОГРН={org.get('ogrn', '')}, Адрес={org.get('address', '')}")
                    found = True
                    break
            if not found:
                traders_data.append([inn, '', ''])
                print(f"Для ИНН={inn} данные не найдены в {info_file}")

        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['INN', 'OGRN', 'Address'])
            writer.writerows(traders_data)

        print(f"Данные успешно сохранены в {output_file}. Записано {len(traders_data)} строк.")

    except FileNotFoundError:
        print(f"Файл {info_file} не найден")
    except json.JSONDecodeError:
        print(f"Ошибка: файл {info_file} не является валидным JSON")
    except Exception as e:
        print(f"Ошибка при обработке {info_file}: {e}")