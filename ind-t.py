#!usr/bin/env python3
# -*- coding: utf-8 -*-


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
            
            for product in products:
                if product.get('name_of_product') == find_name:
                    print(f"Имя:{product.get('name_of_product')}")
                    print(f"Маркет:{product.get('name_of_market')}")
                    print(f"Стоимость:{product.get('value')}")
                    find_count += 1

            if find_count < 0:
                print(f"Товара с именем {find_name} не существует")
                