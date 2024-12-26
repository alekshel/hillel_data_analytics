def sort_by_length(products):
    return sorted(products, key=len)


def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]


def convert_to_uppercase(names):
    return [name.upper() for name in names]


def check_letter_a(words):
    return {word: ('а' in word.lower()) for word in words}


def calculate_total_cost(shopping_list):
    return sum(price * quantity for _, price, quantity in shopping_list)


def count_words(text):
    return len(text.strip().split())


def validate_password(password):
    try:
        if len(password) <= 8:
            raise ValueError("Пароль повинен бути довшим за 8 символів")
        return True
    except ValueError as error:
        return str(error)


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # Завдання 1: Сортування за довжиною
    test_products = ["яблуко", "груша", "апельсин", "ківі"]
    print(f"Відсортовані товари: {sort_by_length(test_products)}")

    # Завдання 2: Фільтрація позитивних чисел
    test_numbers = [-2, 5, 0, -1, 10, 3, -4]
    print(f"Позитивні числа: {filter_positive_numbers(test_numbers)}")

    # Завдання 3: Верхній регістр
    test_names = ["марія", "іван", "петро"]
    print(f"Імена у верхньому регістрі: {convert_to_uppercase(test_names)}")

    # Завдання 4: Перевірка літери 'а'
    test_words = ["книга", "море", "телефон"]
    print("Перевірка на наявність літери 'а':")
    for word, has_a in check_letter_a(test_words).items():
        print(f"{word}: {'містить' if has_a else 'не містить'}")

    # Завдання 5: Обчислення суми покупок
    test_shopping = [
        ("хліб", 20, 2),  # (назва, ціна, кількість)
        ("молоко", 35, 1),
        ("сир", 150, 0.5)
    ]
    print(f"Загальна сума витрат: {calculate_total_cost(test_shopping)} грн")

    # Завдання 6: Підрахунок слів
    test_text = "Це  тестовий   текст для підрахунку   кількості слів"
    print(f"Кількість слів у тексті: {count_words(test_text)}")

    # Завдання 7: Перевірка пароля
    test_passwords = ["123", "password123", "короткий"]
    print("Перевірка паролів:")
    for pwd in test_passwords:
        result = validate_password(pwd)
        print(f"Пароль '{pwd}': {result}")

    # Завдання 8: Середнє значення
    test_values = [10, 15, 20, 25, 30]
    print(f"Середнє значення: {calculate_average(test_values)}")
