#!usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils import command


if __name__ == '__main__':
    list_of_product = []

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

            list_of_product.append(dict_of_product)

            if len(list_of_product) > 1:
                list_of_product.sort(
                    key=lambda item: 
                    item.get('name_of_product', '')
                )
        
        elif command.startswith('info '):
            
            parts = command.split(' ', maxsplit=1)
            
            find_name = parts[1]
            
            a = False
            for i, item in enumerate(list_of_product):
                for j in list_of_product[i]:
                    if list_of_product[i].get(j) == find_name:
                        print("-"* 10)
                        print(
                            f"Имя товара: {list_of_product[i].get(
                                'name_of_product'
                            )}"
                        )
                        print(
                            f"Имя магазина: {list_of_product[i].get(
                                'name_of_market'
                            )}"
                        )
                        print(
                            f"Стоимость: {list_of_product[i].get('value')}"
                        )
                        print(
                            "-" * 10
                        )
                        a = True
            if not a:
                print(f"Товара с именем {find_name} не существует")
                