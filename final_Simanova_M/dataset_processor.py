import json
from typing import Dict, Set
from email_finder import find_emails


def process_dataset(dataset_file: str, output_json: str):

    email_dict: Dict[str, Set[str]] = {}
    processed_records = 0
    skipped_records = 0

    try:
        with open(dataset_file, 'r', encoding='utf-8') as f:
            dataset = json.load(f)

        if not dataset:
            print(f"Ошибка: файл {dataset_file} пустой")
            return

        for record in dataset:
            processed_records += 1
            inn = record.get('publisher_inn')
            msg_text = record.get('msg_text')

            if not inn or not msg_text:
                skipped_records += 1
                print(
                    f"Пропущена запись {processed_records}: "
                    f"отсутствует publisher_inn={inn} или msg_text={msg_text}")
                continue

            if not isinstance(msg_text, str):
                skipped_records += 1
                print(f"Пропущена запись {processed_records}: msg_text не является строкой ({type(msg_text)})")
                continue

            emails = find_emails(msg_text)
            if emails:
                if inn not in email_dict:
                    email_dict[inn] = set()
                email_dict[inn].update(emails)
                print(f"Найдены email для ИНН={inn}: {emails}")

        print(f"\nОбработано записей: {processed_records}")
        print(f"Пропущено записей: {skipped_records}")
        print(f"Найдено ИНН с email-адресами: {len(email_dict)}")

        if not email_dict:
            print(f"Предупреждение: email-адреса не найдены в {dataset_file}")
            return

        serializable_dict = {inn: list(emails) for inn, emails in email_dict.items()}

        print(f"\nСловарь перед сохранением в {output_json}:")
        for inn, emails in serializable_dict.items():
            print(f"ИНН={inn}: {emails}")

        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(serializable_dict, f, ensure_ascii=False, indent=4)

        print(f"Email-адреса успешно сохранены в {output_json}. Записано {len(serializable_dict)} ИНН.")

    except FileNotFoundError:
        print(f"Файл {dataset_file} не найден")
    except json.JSONDecodeError:
        print(f"Ошибка: файл {dataset_file} не является валидным JSON")
    except Exception as e:
        print(f"Ошибка при обработке датасета: {e}")