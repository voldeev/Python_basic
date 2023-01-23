"""
n школярів ділять k яблук порівну, залишок, що не ділиться, залишається в кошику.
Скільки яблук дістанеться кожному школяру? Скільки яблук залишиться у кошику?
Програма отримує на вхід числа n і k і повинна вивести кількість яблук, що шукається (два числа).

Використовувати лише арифметичні оператори (Підказка: знадобляться // та %)
"""

n = int(input("Enter the number of students: "))
k = int(input("Enter the number of apples: "))

amount = k // n     #кількість отриманих яблук на одного учня
print("Each student will receive ", amount, "apples")

residual = k % n    #залишок яблук в корзині
print("It will remain in the basket ", residual, "apples")
