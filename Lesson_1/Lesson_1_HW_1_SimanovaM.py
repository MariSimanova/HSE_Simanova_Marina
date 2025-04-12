# 1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и
# строки и сохраните в переменные, а затем выведите на экран. Используйте функции для консольного ввода input() и
# консольного вывода print(). Попробуйте также через встроенную функцию id() понаблюдать, какие типы объектов могут
# изменяться и сохранять за собой адрес в оперативной памяти.

name = 'Anna'
age = 25
height = 1.60

print("Имя: ", name)
print("Возраст: ", age)
print("Рост: ", height)

print("\n")

user_name = input('Введите ваше имя: ')
user_age = int(input('Введите ваш возраст (число): '))
user_city = input('Введите ваш город: ')

if user_age > 50:
    print(f"Добрый день, уважаемый(-ая) {user_name}! Вам {user_age} лет, и вы живете в {user_city}.")
else:
    print(f"Привет, {user_name}! Тебе {user_age} лет и ты живешь в {user_city}.")

print("\n")

print('ID переменной "name":', id(user_name))
print('ID переменной "age":', id(user_age))
print('ID переменной "city":', id(user_city))
print('ID переменной "height":', id(height))

print("\n")

#Список
numbers_list = [1, 2, 3, 4, 5]

print("ID списка до изменения:", id(numbers_list))
numbers_list.append(6)
numbers_list[0] = 10

print("Список после изменения:", numbers_list)
print("ID списка после изменения:", id(numbers_list))

print("\n")

#Словарь
clients_dict = {'name': 'Олег', 'city': 'Moscow', 'age': 20, 'INN': 456789789}

print("ID словаря до изменения:", id(clients_dict))
clients_dict["age"] = 26
clients_dict["city"] = "Омск"

print("Словарь после изменения:", clients_dict)
print("ID словаря после изменения:", id(clients_dict))

print("\n")

#Множество
numbers_set = {1, 2, 3, 4, 5}

print("ID множества до изменения:", id(numbers_set))
numbers_set.add(6)
numbers_set.remove(3)

print("Множество после изменения:", numbers_set)
print("ID множества после изменения:", id(numbers_set))

print("\n")

# 2. Пользователь вводит время в секундах. Рассчитайте время и сохраните отдельно в каждую переменную количество
# часов, минут и секунд. Переведите время в часы, минуты, секунды и сохраните в отдельных переменных. Используйте
# приведение типов для перевода строк в числовые типы. Предусмотрите проверку строки на наличие только числовых
# данных через встроенный строковый метод .isdigit(). Выведите рассчитанные часы, минуты и секунды по отдельности в
# консоль.

seconds_input=input("Введите время в секундах:")
if seconds_input.isdigit():
    total_seconds=int(seconds_input)
    hours=total_seconds//3600
    remaining_seconds=total_seconds%3600
    minutes=remaining_seconds//60
    seconds=remaining_seconds%60

    print(f"Часы: {hours}")
    print(f"Минуты: {minutes}")
    print(f"Секунды: {seconds}")
else:
    print("Ошибка:введите только числовые данные.")

print("\n")

# 3. Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# Выведите данные в консоль.

n=input('Введите число от 1 до 9: ')

if n.isdigit() and len(n) == 1 and 1 <= int(n) <= 9:
    n = int(n)
    nn = int(f"{n}{n}")
    nnn = int(f"{n}{n}{n}")
    result=n+nn+nnn

    print(f"Сумма чисел {n} + {nn} + {nnn} = {result}")
else:
    print("Ошибка: Введите число от 1 до 9.")