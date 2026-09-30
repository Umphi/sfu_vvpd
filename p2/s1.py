from collections import Counter
import sys

class Task1:
    def __init__(self):
        self.list_a = []
        self.list_b = []

    def get_list_a(self):
        return self.list_a

    def get_list_b(self):
        return self.list_b

    def add_item_a(self, item):
        self.list_a.append(item)

    def add_item_b(self, item):
        self.list_b.append(item)

    def clear_a(self):
        self.list_a = []

    def clear_b(self):
        self.list_b = []

    @staticmethod
    def find_duplicates(items):
        counts = Counter(items)
        duplicates = [item for item, count in counts.items() if count > 1]
        return duplicates

    @staticmethod
    def exclude_items(first_list, second_list):
        return [item for item in first_list if item not in second_list]


def main():
    task = Task1()

    while True:
        print("\n"*50)
        print("Задание 1.26. Юркевич И.А.")
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
                print("Вы можете вводить элементы через Enter или ввести \"return\" для возврата: ")
                element = "-1"
                while element != "return":
                    element = input()
                    if len(element) > 0 and element != "return":
                        task.add_item_a(element)
                
            case "2":
                print("Вы можете вводить элементы через Enter или ввести \"return\" для возврата: ")
                element = "-1"
                while element != "return":
                    element = input()
                    if len(element) > 0 and element != "return":
                        task.add_item_b(element)
            case "3":
                answer = task.exclude_items(
                    task.find_duplicates(task.get_list_a()), task.get_list_b()
                )
                print("Повторяющиеся элементы массива A, которых нет в массиве B:")
                print(answer)
                print("Нажмите Enter для возврата в меню...")
                input()
            case "4":
                task.clear_a()
                task.clear_b()

if __name__ == "__main__":
    main()
