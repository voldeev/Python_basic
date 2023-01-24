"""
Дано ціле, позитивне, тризначне число. Наприклад: 123, 867, 374.
Необхідно його перевернути. Наприклад, якщо ввели число 123, то має вийти на виході ЧИСЛО 321.
ВАЖЛИВО! Працювати лише з числами. Рядки, оператор IF та цикли використовувати НЕ МОЖНА!
На виході обов'язково має бути число!!!
"""

num = int(input("Enter a three-digit number: "))

num_3 = num % 10                    #Третя цифра
num_2 = num % 100 // 10             #Друга цифра
num_1 = num % 1000 // 100           #Перша цифра

print(100 * num_3 + 10 * num_2 + num_1)
