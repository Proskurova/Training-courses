# Задача №2: Определить существование треугольника и его тип
AB = int(input('Введите сторону АВ:'))
BC = int(input('Введите сторону BC:'))
CA = int(input('Введите сторону CA:'))
if AB+BC<=CA or BC+CA<=AB or AB+CA<=BC:
    print('Не является треугольникам')
elif AB==BC==CA:
    print('Равносторонний треугольник')
elif AB==BC!=CA or BC==CA!=AB:
    print('Равнобедренный треугольник')
elif AB!=BC!=CA:
    print('Разносторонний треугольник')





