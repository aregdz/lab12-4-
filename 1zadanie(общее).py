#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
