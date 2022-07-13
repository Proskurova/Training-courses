# 5.Клиент приходит в кондитерскую.
# Он хочет приобрести один или несколько видов продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).
shop = {"карамель": ['сахар,патока,молоко сухое,жир растительный,лецитин,водa', 3.25, 7500],
        "чизкейк": ['сливочный сыр,яйца,сахар,корица,имбирь,кукурузный крахмал', 4.15, 6200],
        "вафли": ['творог,сливочное масло,сахар,мука,яйцо,соль,ванилин,разрыхлитель', 3.85, 9000],
        "зефир": ['сахар-песок,сода,лимонная кислота,желатин,ванилин', 3.12, 5000],
         "кекс": ['мука,картофельный крахмал,изюм,масла,сахар,яица,сода', 4.55, 10000]
        }
print("Ассортимент кондитерской:")
for sh in shop:
    print(sh, "-", shop[sh][1], "за 100гр.; Остатки товара", (shop[sh][2])/1000, "кг")
print("Для окончания покупок вместо товара нажмите 'н'")
count = 0
cheque = []
i = 0
while True:
    product = input("Продукт:")
    cheque.append(product)
    if product == "н":
        cheque.remove("н")
        print("Стоимость ваших десертов({0}) = {1:2f}".format(cheque, count))
        print("Остатки кондитерской:")
        for j in shop:
            print(j, "-", shop[j][1], "за 100гр.; Остатки товара", (shop[j][2]) / 1000, "кг")
        print("Спасибо за покупку! Будем рады видеть вас снова!")
        break
    print("Хотите посмотреть состав?")
    a = input("Напишите 'да' или 'нет':")
    if a == 'да':
        print("Состав {0}:".format(product), shop[product][0])
    else:
        print("Продолжаем покупки!")
    pieces = int(input("Количество в граммах:"))
    for pr, pi in shop.items():
        if pr == product:
            if pieces > shop[pr][2]:
                print("Этого десерта нет столько в наличии, введите соглано остаткам!")
                pieces = 0
                break
            price = float((shop[pr][1]*pieces)/100)
            count +=price
            remains = shop[pr][2]-pieces
            shop[pr][2] = remains
            if remains == 0:
                print("Этого товара больше нет в наличии!")
        else:
            continue
        i += 1