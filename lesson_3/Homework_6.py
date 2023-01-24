"""
Шаховий кінь ходить буквою "Г" - на дві клітинки по вертикалі в будь-якому напрямку і на одну клітинку по горизонталі,
або навпаки.
Дано дві різні клітини шахової дошки, визначте, чи може кінь потрапити з першої клітини на другу одним ходом.
"""

x1 = int(input())                                   # Вихідні координати по горизонталі
y1 = int(input())                                   # Вихідні координати по вертикалі
x2 = int(input())                                   # Кінцеві координати по горизонталі
y2 = int(input())                                   # Кінцеві координати по вертикалі
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
