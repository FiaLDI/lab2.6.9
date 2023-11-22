#!usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils import command
from queue import Empty
import sys


if __name__ == '__main__':
    towars = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Имя товара: ")
            marketName = input("Имя магазина: ")
            st = int(input("Стоимость товара: "))

            towar = {
                'name':name,
                'marketName':marketName,
                'st':st
            }

            towars.append(towar)

            if len(towars) > 1:
                towars.sort(key=lambda item: item.get('name', ''))
        
        elif command == 'info':
            nameTowar = input('Введите название: ')
            
            a = False
            for i, item in enumerate(towars):
                for j in towars[i]:
                    if towars[i].get(j) == nameTowar:
                        print("-"* 10)
                        print(f"Имя товара: {towars[i].get('name')}")
                        print(f"Имя магазина: {towars[i].get('marketName')}")
                        print(f"Стоимость: {towars[i].get('st')}")
                        print("-" * 10)
                        a = True
            if a == False:
                print(f"Товара с именем {nameTowar} не существует")
                