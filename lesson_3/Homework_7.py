"""
Написати програму визначальну високосний рік.
Користувач вводить номер року, програма повинна відповісти високосний рік чи ні.
Алгоритм перевірки високосного року можна переглянути тут
(https://uk.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D0%B8%D0%B9_%D1%80%D1%96%D0%BA),
розділ "Григоріанський календар"
"""

year = int(input("Enter the year in XXXX format: "))

if year // 4 != 0 and year % 4 == 0:
    print("This is a leap year")
else:
    print("This year is not a leap year")
