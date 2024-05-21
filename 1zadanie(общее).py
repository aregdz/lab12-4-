#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
#Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
#соединение, строк. В остальных случаях введенные числа суммируются.

def main():
    try:
        value1 = input("Введите первое значение: ")
        value2 = input("Введите второе значение: ")

        num1 = float(value1)
        num2 = float(value2)

        result = num1 + num2
        print("Результат сложения:", result)
    except ValueError:
        result = value1 + value2
        print("Результат конкатенации:", result)


if __name__ == "__main__":
    main()
