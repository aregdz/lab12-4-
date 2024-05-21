#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# задание: Изучить возможности модуля logging. Добавить для предыдущего задания вывод в файлы лога
# даты и времени выполнения пользовательской команды с точностью до миллисекунды.

import logging
import sys


class FlightManager:
    def __init__(self):
        self.aircrafts = []

    def add(self):
        """ "
        Метод для добавления информации о новых рейсах
        """
        # Запросить данные о работнике.
        name = input("Название пункта назначения рейса? ")
        number = int(input("Номер рейса? "))
        tip = input("Тип самолета? ")
        # Создать словарь.
        i = {
            "name": name,
            "number": number,
            "tip": tip,
        }

        self.aircrafts.append(i)
        # Отсортировать список в случае необходимости.
        if len(self.aircrafts) > 1:
            self.aircrafts.sort(key=lambda item: item.get("name", ""))

    def list(self):
        """ "
        Метод для вывода списка добавленных рейсов
        """
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4, "-" * 30, "-" * 20, "-" * 8
        )
        print(line)

        # Вывести данные о всех сотрудниках.
        for idx, i in enumerate(self.aircrafts, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {:>8} |".format(
                    idx,
                    i.get("name", ""),
                    i.get("number", ""),
                    i.get("tip", ""),
                )
            )
        print(line)

    def select(self):
        """ ""
        Метод для получения номера рейса и пункта назначения по заданному типу самолёта.
        """
        # Разбить команду на части для выделения номера года.
        parts = input("Введите значение: ")
        # Проверить сведения работников из списка.
        count = 0

        for i in self.aircrafts:
            for k, v in i.items():

                if v == parts:
                    print("Пункт назначения - ", i["name"])
                    print("Номер рейса - ", i["number"])
                    count += 1
        # Если счетчик равен 0, то работники не найдены.
        if count == 0:
            print("Рейс с заданным типом самолёта не найден.")

    def help(self):
        """ "
        Метод для вывода списка команд
        """
        print("Список команд:\n")
        print("add - добавить рейс;")
        print("list - вывести список рейсов;")
        print(
            "select <тип> - вывод на экран пунктов назначения и номеров рейсов для данного типа самолёта"
        )
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")


if __name__ == "__main__":

    logging.basicConfig(
        filename="fly2.log",
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    flight_manager = FlightManager()

    while True:
        try:
            # Запросить команду из терминала.
            command = input(">>> ").lower()
            # Выполнить действие в соответствие с командой.

            match command:
                case "exit":
                    break

                case "add":
                    flight_manager.add()

                case "list":
                    flight_manager.list()

                case "select":
                    flight_manager.select()

                case "help":
                    flight_manager.help()

                case _:
                    print("Команда не найдена")

        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)
