#!usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    school = {
        "1а": 1000,
        "1б": 1000,
        "1в": 1000,
        "2а": 1000,
        "3а": 1000,
        "4а": 1000,
        "5а": 1000,
        "6а": 1000,
        "7а": 1000
    }

    class_of_school = input("Введите класс: ")
    value_of_student = int(input("Введите количество учеников: "))
    school[class_of_school] = value_of_student

    new_class_of_school = input("Введите название нового класса: ")
    new_class_value_of_student = int(input(
        "Введите количество учеников в новом классе: ")
    )
    school.setdefault(
        new_class_of_school,
        new_class_value_of_student
    )

    del_of_class_value = input(
        "Введите класс, который необходимо удалить: "
    )

    del del_of_class_value
    print(school)
    print(sum(school.values()))

