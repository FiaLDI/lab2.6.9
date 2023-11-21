#!usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    school = {
        "1a": 1000,
        "1б": 1000,
        "1в": 1000,
        "2a": 1000,
        "3a": 1000,
        "4a": 1000,
        "5a": 1000,
        "6a": 1000,
        "7a": 1000
    }

    class_of_school = input("Введите класс: ")
    value_of_student = int(input("Введите количество учеников: "))
    school[class_of_school] = value_of_student

    new_class_of_school = input("Введите название нового класса: ")
    new_class_value_of_student = int(input(
        "Введите количество учеников в новом классе: ")
    )

    del_of_class_value = input(
        "Введите класс, который необходимо удалить: "
    )

    del del_of_class_value

    print(school)

