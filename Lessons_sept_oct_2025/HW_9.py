import random
import time

# Генерация массива с случайным шагом от 3 до 5
def generate_sorted_array(start, end, step_min, step_max):
    step = random.randint(step_min, step_max)
    return list(range(start, end + 1, step))

# Линейный поиск
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Бинарный поиск
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    start, end = 10, 250_000
    step_min, step_max = 3, 5

    # Тест 1: с шагом 3
    random.seed(42)
    sorted_array = generate_sorted_array(start, end, step_min, step_max)
    step = sorted_array[1] - sorted_array[0]
    print(f"\nТест 1: Массив с шагом {step}, длина {len(sorted_array)}")
    random_numbers = [random.randint(10, 250_000) for _ in range(5)]
    print(f"Случайные числа: {random_numbers}")
    print("Линейный поиск:")
    start_time = time.time()
    for num in random_numbers:
        result = linear_search(sorted_array, num)
        print(f"Число {num}: {'найдено на индексе ' + str(result) if result != -1 else 'не найдено'}")
    print(f"Время: {time.time() - start_time:.6f} секунд")
    print("Бинарный поиск:")
    start_time = time.time()
    for num in random_numbers:
        result = binary_search(sorted_array, num)
        print(f"Число {num}: {'найдено на индексе ' + str(result) if result != -1 else 'не найдено'}")
    print(f"Время: {time.time() - start_time:.6f} секунд")

    # Тест 2: Крайние значения (минимальное и максимальное)
    print("\nТест 2: Крайние значения")
    test_numbers = [10, 250_000, 250_001]
    print(f"Числа для поиска: {test_numbers}")
    print("Линейный поиск:")
    start_time = time.time()
    for num in test_numbers:
        result = linear_search(sorted_array, num)
        print(f"Число {num}: {'найдено на индексе ' + str(result) if result != -1 else 'не найдено'}")
    print(f"Время: {time.time() - start_time:.6f} секунд")
    print("Бинарный поиск:")
    start_time = time.time()
    for num in test_numbers:
        result = binary_search(sorted_array, num)
        print(f"Число {num}: {'найдено на индексе ' + str(result) if result != -1 else 'не найдено'}")
    print(f"Время: {time.time() - start_time:.6f} секунд")

    # Тест 3: Пустой массив
    print("\nТест 3: Пустой массив")
    empty_array = []
    test_numbers = [10, 100]
    print(f"Числа для поиска: {test_numbers}")
    print("Линейный поиск:")
    start_time = time.time()
    for num in test_numbers:
        result = linear_search(empty_array, num)
        print(f"Число {num}: {'найдено на индексе ' + str(result) if result != -1 else 'не найдено'}")
    print(f"Время: {time.time() - start_time:.6f} секунд")
    print("Бинарный поиск:")
    start_time = time.time()
    for num in test_numbers:
        result = binary_search(empty_array, num)
        print(f"Число {num}: {'найдено на индексе ' + str(result) if result != -1 else 'не найдено'}")
    print(f"Время: {time.time() - start_time:.6f} секунд")

    # Тест 4: Разный шаг (шаг 5)
    random.seed(123)
    sorted_array = generate_sorted_array(start, end, step_min, step_max)
    step = sorted_array[1] - sorted_array[0]
    print(f"\nТест 4: Массив с шагом {step}, длина {len(sorted_array)}")
    random_numbers = [15, 250, 50000]
    print(f"Числа для поиска: {random_numbers}")
    print("Линейный поиск:")
    start_time = time.time()
    for num in random_numbers:
        result = linear_search(sorted_array, num)
        print(f"Число {num}: {'найдено на индексе ' + str(result) if result != -1 else 'не найдено'}")
    print(f"Время: {time.time() - start_time:.6f} секунд")
    print("Бинарный поиск:")
    start_time = time.time()
    for num in random_numbers:
        result = binary_search(sorted_array, num)
        print(f"Число {num}: {'найдено на индексе ' + str(result) if result != -1 else 'не найдено'}")
    print(f"Время: {time.time() - start_time:.6f} секунд")