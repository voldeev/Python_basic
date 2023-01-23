"""
У школі вирішили набрати три нові математичні класи.
Так як заняття з математики у них відбуваються в один і той же час,
було вирішено виділити кабінет для кожного класу і купити нові парти.
За кожною партою може сидіти не більше двох учнів. Відомо кількість учнів у кожному із трьох класів.
Скільки всього потрібно закупити парт, щоб їх вистачило на всіх учнів?
Програма отримує на вхід три натуральні числа: кількість учнів у кожному з трьох класів.

Використовувати лише арифметичні оператори. (Підказка: знадобляться // + та %) Оператор IF використовувати не можна.
"""

first_class = int(input("Number of students in the first grade: "))
second_class = int(input("Number of students in the second grade: "))
third_class = int(input("Number of students in the third grade: "))

num_of_desks = (first_class // 2 + second_class // 2 + third_class // 2 + first_class % 2 + second_class % 2 + third_class % 2)
print("Need to buy", num_of_desks, "study desks")
