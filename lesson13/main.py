def calculate_list_sum(input_numbers):
    return sum(input_numbers)


def get_unique_numbers(input_numbers):
    return list(dict.fromkeys(input_numbers))


def find_number_in_tuple(input_tuple):
    try:
        return input_tuple.index(5)
    except ValueError:
        return "Число 5 не знайдено в кортежі"


def get_sets_intersection(first_set, second_set):
    return first_set.intersection(second_set)


def add_student_grade(grades_dict, student_name, grade):
    grades_dict[student_name] = grade
    return grades_dict


def get_reversed_list(input_numbers):
    return input_numbers[::-1]


def get_all_combinations(first_list, second_list):
    return [(x, y) for x in first_list for y in second_list]


def remove_number_from_set(input_set):
    input_set.discard(3)
    return input_set


def get_sorted_dict(input_dict):
    return dict(sorted(input_dict.items(), key=lambda x: x[1]))


def merge_lists(first_list, second_list):
    return first_list + second_list


def separate_by_type(mixed_data):
    type_separated = {}

    for item in mixed_data:
        type_name = type(item).__name__
        if type_name not in type_separated:
            type_separated[type_name] = []
        type_separated[type_name].append(item)

    return type_separated


if __name__ == "__main__":
    # Завдання 1: Сума елементів списку
    test_numbers = [1, 2, 3, 4, 5]
    print(f"Сума списку {test_numbers}: {calculate_list_sum(test_numbers)}")

    # Завдання 2: Видалення дублікатів
    duplicate_numbers = [1, 2, 2, 3, 3, 4, 5, 5]
    print(f"Список без дублікатів: {get_unique_numbers(duplicate_numbers)}")

    # Завдання 3: Пошук в кортежі
    test_tuple = (1, 2, 5, 4, 5)
    print(f"Індекс першого числа 5: {find_number_in_tuple(test_tuple)}")

    # Завдання 4: Перетин множин
    test_set1 = {1, 2, 3, 4}
    test_set2 = {3, 4, 5, 6}
    print(f"Спільні елементи множин: {get_sets_intersection(test_set1, test_set2)}")

    # Завдання 5: Додавання до словника
    student_grades = {"Іван": 95, "Марія": 98}
    print(f"Оновлений словник студентів: {add_student_grade(student_grades, 'Петро', 88)}")

    # Завдання 6: Зворотний список
    original_numbers = [1, 2, 3, 4, 5]
    print(f"Зворотній список: {get_reversed_list(original_numbers)}")

    # Завдання 7: Комбінації елементів
    first_input = [1, 2]
    second_input = ['A', 'B']
    print(f"Всі можливі комбінації: {get_all_combinations(first_input, second_input)}")

    # Завдання 8: Видалення з множини
    test_set = {1, 2, 3, 4, 5}
    print(f"Множина після видалення числа 3: {remove_number_from_set(test_set)}")

    # Завдання 9: Сортування словника
    product_prices = {"Яблука": 25, "Банани": 30, "Апельсини": 20}
    print(f"Відсортований словник: {get_sorted_dict(product_prices)}")

    # Завдання 10: Конкатенація списків
    list_one = [1, 2, 3]
    list_two = [4, 5, 6]
    print(f"Об'єднаний список: {merge_lists(list_one, list_two)}")

    # Додаткове завдання: Розділення за типами
    mixed_test_data = [1, "hello", [1, 2], 3.14, (1, 2), {1, 2}, {"a": 1}]
    print("Розділення за типами:")
    separated_data = separate_by_type(mixed_test_data)
    for data_type, items in separated_data.items():
        print(f"{data_type}: {items}")
