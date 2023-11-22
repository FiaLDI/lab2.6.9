#!usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils import command


if __name__ == '__main__':
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name_of_product = input("Имя товара: ")
            name_of_market = input("Имя магазина: ")
            value = int(input("Стоимость товара: "))

            dict_of_product = {
                'name_of_product':name_of_product,
                'name_of_market':name_of_market,
                'value':value
            }

            products.append(dict_of_product)

            if len(products) > 1:
                products.sort(
                    key=lambda item:item.get('name_of_product', '')
                )
        
        elif command.startswith('info '):
            
            parts = command.split(' ', maxsplit=1)
            
            find_name = parts[1]
            
            find_count = 0
            for i, item in enumerate(products):
                for j in products[i]:
                    if products[i].get(j) == find_name:
                        print("-"* 10)
                        print(
                            f"Товара: {products[i].get('name_of_product')}"
                        )
                        print(
                            f"Магазин: {products[i].get('name_of_market')}"
                        )
                        print(
                            f"Стоимость: {products[i].get('value')}"
                        )
                        print( "-" * 10)
                        find_count += 1
            if not find_count:
                print(f"Товара с именем {find_name} не существует")
                