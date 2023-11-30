#!usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name_of_product = input("Название товара: ")
            name_of_market = input("Название магазина:  ")
            value = int(input("Стоимость: "))  

            product = {
                'name_of_product': name_of_product,
                'name_of_market':name_of_market,
                'value':value
            }

            products.append(product)

            if len(products) > 1:
                products.sort(
                    key=lambda item: item.get('name_of_product', '')
                )
        
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print( '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Название товара",
                    "Название магазина",
                    "Стоимость"
                )
            )
            print(line)
            
            for idx, product in enumerate(products, 1):
                print( '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        product.get('name_of_product', ''),
                        product.get('name_of_market', ''),
                        product.get('value', 0)
                    )
                )
                
            print(line)

        elif command.startswith('info '):            
            parts = command.split(' ', maxsplit=1)
            
            find_name = parts[1]
            
            find_count = 0
            
            for product in products:
                if product.get('name_of_product') == find_name:
                    find_count += 1
                    print ( ' | {:<30} | {:<20} | {:>8} |'.format(
                            product.get('name_of_product', ''),
                            product.get('name_of_market', ''),
                            product.get('value', '')
                        )
                    )
            
            if find_count == 0:
                print("Товар с заданным именем не найден")
        elif command == 'help':

            print("Список команд:\n")
            print("add - добавить товар;")
            print("list - вывести список товаров;")
            print("info <товар> - вывести информацию о товаре;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
    