""" Юркевич И.А. ЗКИ25-18Б Задание 2. Секция 2. Вариант 26 """
from collections import Counter
import sys

class Task2:
    """
    Задание 2.26
    Элементы, которые присутствуют в нескольких экземплярах
    в массиве А, но отсутствуют в массиве В
    """
    def __init__(self):
        self.list_a = []
        self.list_b = []

    def get_list_a(self):
        """ Вывод списка A """
        return self.list_a

    def get_list_b(self):
        """ Вывод списка B """
        return self.list_b

    def add_item_a(self, item):
        """ Добавить элемент в список A """
        self.list_a.append(item)

    def add_item_b(self, item):
        """ Добавить элемент в список B """
        self.list_b.append(item)

    def clear_a(self):
        """ Очистить список A """
        self.list_a = []

    def clear_b(self):
        """ Очистить список B """
        self.list_b = []

    def perform(self):
        """ Выполнить задание """
        return self.exclude_items(self.find_duplicates(self.list_a), self.list_b)

    @staticmethod
    def find_duplicates(items):
        """ Найти повторяющиеся в списке """
        counts = Counter(items)
        duplicates = [item for item, count in counts.items() if count > 1]
        return duplicates

    @staticmethod
    def exclude_items(first_list, second_list):
        """ Исключить элементы второго списка из первого """
        return [item for item in first_list if item not in second_list]


def main():
    """ Главная функция """
    task = Task2()

    while True:
        print("\n"*50)
        print("Задание 2.26. Юркевич И.А.")
        print(f"A: {task.get_list_a()}")
        print(f"B: {task.get_list_b()}")
        print("\t1. Добавить элементы в массив A" \
        "\n\t2. Добавить элементы в массив B" \
        "\n\t3. Выполнить задание" \
        "\n\t4. Очистить списки" \
        "\n\t0. Выход"
        )
        choose = "-1"
        while choose not in "01234":
            print("Выберите пункт меню: ")
            choose = input()

        match choose:
            case "0":
                sys.exit(0)
            case "1":
                print("Вы можете вводить элементы через Enter " \
                "или ввести return для возврата: ")
                element = "-1"
                while element != "return":
                    element = input()
                    if len(element) > 0 and element != "return":
                        task.add_item_a(element)
            case "2":
                print("Вы можете вводить элементы через Enter " \
                "или ввести return для возврата: ")
                element = "-1"
                while element != "return":
                    element = input()
                    if len(element) > 0 and element != "return":
                        task.add_item_b(element)
            case "3":
                answer = task.perform()
                print("Элементы, которые присутствуют в нескольких экземплярах " \
                "в массиве А, но отсутствуют в массиве В:")
                print(answer)
                print("Нажмите Enter для возврата в меню...")
                input()
            case "4":
                task.clear_a()
                task.clear_b()

if __name__ == "__main__":
    main()
