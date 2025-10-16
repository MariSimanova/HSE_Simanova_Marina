#Задача №1

def fib(n):
    if n <= 0:
        return

    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1

#пример
n = 10
for num in fib(n):
    print(num, end=' ')

#Задача №2

def roman_to_decimal(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}

    result = 0
    explanation_parts = []

    i = 0
    while i < len(s):
        if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
            value = roman_values[s[i + 1]] - roman_values[s[i]]
            explanation_parts.append(f"{s[i]}{s[i + 1]} = {value}")
            result += value
            i += 2
        else:
            value = roman_values[s[i]]
            explanation_parts.append(f"{s[i]} = {value}")
            result += value
            i += 1

    explanation = ", ".join(explanation_parts)
    return result, explanation


#пример

if __name__ == "__main__":
    res, exp = roman_to_decimal("III")
    print(f"Вход: III, Выход: {res}, Объяснение: {exp}")

    res, exp = roman_to_decimal("LVIII")
    print(f"Вход: LVIII, Выход: {res}, Объяснение: {exp}")

    res, exp = roman_to_decimal("MCMXCIV")
    print(f"Вход: MCMXCIV, Выход: {res}, Объяснение: {exp}")

# Задача №3

def is_monotonic(nums):
    if len(nums) <= 2:
        return True

    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing

#пример
if __name__ == "__main__":
    print(is_monotonic([1, 2, 2, 3]))
    print(is_monotonic([6, 5, 4, 4]))
    print(is_monotonic([1, 3, 2]))