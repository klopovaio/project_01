# Задача 1.4.



# Есть словарь кодов товаров titles



titles = {

    'Кроссовки тип 3 (Adidas)': '100000110',

    'Мячик тип 2 (Adidas)': '100000146',

    'Кепка тип 1 (Adidas)': '100000149',

    'Ремень тип 2 (Nike)': '100000194',

    'Футболка тип 1 (Adidas)': '100000224',

    'Шапка тип 5 (Puma)': '100000280',

}



# Товары находятся на складе и сохранены в виде словаря списков словарей,

# которые отражают количество товаров в магазине по каждому коду.



store = {

    '100000110': [{'quantity': 31, 'price': 1637}],

    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],

    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],

    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],

    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],

    '100000280': [{'quantity': 26, 'price': 175}, ]

}



# Рассчитайте на какую сумму лежит каждого товара на складе.

#

# Вывести суммарную стоимость каждого товара в магазине в формате:

# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"



# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"



kross_code = titles['Кроссовки тип 3 (Adidas)']

kross_item = store[kross_code][0]

kross_quantity = kross_item['quantity']

kross_price = kross_item['price']

kross_cost = kross_quantity * kross_price

print('Кроссовки тип 3 (Adidas) -', kross_quantity, 'шт, стоимость', kross_cost, 'руб')



ball_code = titles['Мячик тип 2 (Adidas)']

ball_item = store[ball_code][0]

ball_quantity = ball_item['quantity']

ball_price = ball_item['price']

ball_cost = ball_quantity * ball_price

print('Мячик тип 2 (Adidas) -', ball_quantity, 'шт, стоимость', ball_cost, 'руб')



cap_code = titles['Кепка тип 1 (Adidas)']

cap_item = store[cap_code][0]

cap_quantity = cap_item['quantity']

cap_price = cap_item['price']

cap_cost = cap_quantity * cap_price

print('Кепка тип 1 (Adidas) -', cap_quantity, 'шт, стоимость', cap_cost, 'руб')



belt_code = titles['Ремень тип 2 (Nike)']

belt_item = store[belt_code][0]

belt_quantity = belt_item['quantity']

belt_price = belt_item['price']

belt_cost = belt_quantity * belt_price

print('Ремень тип 2 (Nike) -', belt_quantity, 'шт, стоимость', belt_cost, 'руб')





f_code = titles['Футболка тип 1 (Adidas)']

f_item = store[f_code][0]

f_quantity = f_item['quantity']

f_price = f_item['price']

f_cost = f_quantity * f_price

print('Футболка тип 1 (Adidas) -', f_quantity, 'шт, стоимость', f_cost, 'руб')



hat_code = titles['Шапка тип 5 (Puma)']

hat_item = store[hat_code][0]

hat_quantity = hat_item['quantity']

hat_price = hat_item['price']

hat_cost = hat_quantity * hat_price

print('Шапка тип 5 (Puma) -', hat_quantity, 'шт, стоимость', hat_cost, 'руб')