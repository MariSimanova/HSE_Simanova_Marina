import os
from traders_processor import process_traders_with_info
from dataset_processor import process_dataset
from email_finder import find_emails

if __name__ == "__main__":
    traders_input = "traders.txt"
    traders_info = "traders.json"
    traders_output = "traders.csv"
    dataset_file = "1000_efrsb_messages.json"
    emails_output = "emails.json"

    print("Проверка файлов...")
    if not os.path.exists(traders_input):
        print(f"Ошибка: файл {traders_input} не найден в папке проекта")
    elif not os.path.exists(traders_info):
        print(f"Ошибка: файл {traders_info} не найден в папке проекта")
    elif not os.path.exists(dataset_file):
        print(f"Ошибка: файл {dataset_file} не найден в папке проекта")
    else:
        print("\nОбработка traders.txt с данными из traders.json...")
        process_traders_with_info(traders_input, traders_info, traders_output)

        print("\nОбработка датасета ЕФРСБ (1000_efrsb_messages.json)...")
        process_dataset(dataset_file, emails_output)

