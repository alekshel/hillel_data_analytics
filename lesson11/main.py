def arithmetic_operations():
   print("Завдання 2:")

   result = 2 * 3
   print(f"2 * 3 = {result}, тип: {type(result)}")

   result = (3 * 3 + 8) / 3
   print(f"(3 * 3 + 8) / 3 = {result}, тип: {type(result)}")

   result = 8 // 3
   print(f"8 // 3 = {result}, тип: {type(result)}")

   result = 8 % 3
   print(f"8 % 3 = {result}, тип: {type(result)}")

   result = 5 ** 2
   print(f"5 ** 2 = {result}, тип: {type(result)}")

   result = "Hello " + "world"
   print(f"'Hello ' + 'world' = {result}, тип: {type(result)}")

   result = "Python" * 5
   print(f"'Python' * 5 = {result}, тип: {type(result)}")

   result = 5 < 9
   print(f"5 < 9 = {result}, тип: {type(result)}")

def text_variables():
   print("\nЗавдання 3:")
   first_name = 'John'
   last_name = "Doe"
   print(f"Повне ім'я: {first_name} {last_name}")

def slice_operations():
   print("\nЗавдання 4:")
   zen = "Simple is better than complex"

   print(f"Перші 10 символів: {zen[:10]}")

   print(f"10 символів з 3-го: {zen[3:13]}")

   print(f"Останні 10 символів: {zen[-10:]}")

   print(f"Зворотній порядок: {zen[::-1]}")

   print(f"Парні індекси: {zen[::2]}")
   print(f"Непарні індекси: {zen[1::2]}")

def comparison_operations():
   print("\nЗавдання 5:")
   num1 = 75
   num2 = 50

   print(f"{num1} > {num2}: {num1 > num2}")
   print(f"{num1} < {num2}: {num1 < num2}")
   print(f"{num1} == {num2}: {num1 == num2}")
   print(f"{num1} != {num2}: {num1 != num2}")

   is_greater_and_positive = num1 > num2 and num1 > 0
   print(f"num1 більше num2 і додатне: {is_greater_and_positive}")

   is_less_or_fifty = num1 < 100 or num1 == 50
   print(f"num1 менше 100 або дорівнює 50: {is_less_or_fifty}")

def main():
   arithmetic_operations()
   text_variables()
   slice_operations()
   comparison_operations()

if __name__ == "__main__":
   main()