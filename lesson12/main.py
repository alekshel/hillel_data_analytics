def task1():
    # Виводить числа від 1 до 100, що діляться на 5
    print("\nЗавдання 1:")
    for num in range(1, 101):
        if num % 5 == 0:
            print(num, end=" ")


def task2():
    # Виводить парні числа від 1 до 20
    print("\nЗавдання 2:")
    for num in range(2, 21, 2):
        print(num, end=" ")


def task3():
    # Перевіряє парність/непарність введеного числа
    print("\nЗавдання 3:")
    number = int(input("Введіть число: "))
    print("Парне" if number % 2 == 0 else "Непарне")


def task4():
    # Обчислює суму чисел від 1 до 50
    print("\nЗавдання 4:")
    print(f"Сума: {sum(range(1, 51))}")


def task5():
    # Виводить числа більші за 5 зі списку 1-10
    print("\nЗавдання 5:")
    numbers = list(range(1, 11))
    print([num for num in numbers if num > 5])


def task6():
    # Перевіряє чи число понад 10
    print("\nЗавдання 6:")
    number = int(input("Введіть число: "))
    print("Більше 10" if number > 10 else "Менше або дорівнює 10")


def task7():
    # Таблиця множення для 3
    print("\nЗавдання 7:")
    for i in range(1, 11):
        print(f"3 x {i} = {3 * i}")


def task8():
    # Вітає користувача за іменем
    print("\nЗавдання 8:")
    name = input("Введіть ваше ім'я: ")
    print(f"Привіт, {name}!")


def task9():
    # Числа від 1 до 100, що не діляться на 3 або 5
    print("\nЗавдання 9:")
    print([num for num in range(1, 101) if num % 3 != 0 and num % 5 != 0])


def task10():
    # Перевіряє чи рядок містить тільки літери
    print("\nЗавдання 10:")
    text = input("Введіть текст: ")
    print("Тільки літери" if text.isalpha() else "Містить інші символи")


def task11():
    # Числа від 1 до 50, кратні 7
    print("\nЗавдання 11:")
    print([num for num in range(1, 51) if num % 7 == 0])


def task12():
    # Визначає знак числа
    print("\nЗавдання 12:")
    number = float(input("Введіть число: "))
    if number > 0:
        print("Додатне")
    elif number < 0:
        print("Від'ємне")
    else:
        print("Нуль")


def task13():
    # Таблиця множення для введеного числа
    print("\nЗавдання 13:")
    number = int(input("Введіть число: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


def task14():
    # Сума введених чисел
    print("\nЗавдання 14:")
    total = 0
    while True:
        num = input("Введіть число (або 'q' для завершення): ")
        if num.lower() == 'q':
            break
        total += float(num)
    print(f"Сума: {total}")


def task15():
    # Перевіряє чи число просте
    print("\nЗавдання 15:")
    number = int(input("Введіть число: "))
    if number < 2:
        print("Не просте")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Не просте")
            break
    else:
        print("Просте")


def main():
    tasks = [
        task1, task2, task3, task4, task5,
        task6, task7, task8, task9, task10,
        task11, task12, task13, task14, task15
    ]

    while True:
        print("\nВиберіть завдання (1-15) або 0 для виходу:")
        choice = input("Ваш вибір: ")
        if choice == '0':
            break
        try:
            task_num = int(choice)
            if 1 <= task_num <= 15:
                tasks[task_num - 1]()
            else:
                print("Виберіть число від 1 до 15")
        except ValueError:
            print("Введіть коректне число")


if __name__ == "__main__":
    main()