from tasks import add_task, show_tasks, delete_task

def menu():
    while True:
        print("\n--- TO-DO APP ---")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выход")

        choice = input("Выбери действие: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Введите задачу: ")
            add_task(task)
        elif choice == "3":
            index = int(input("Введите номер задачи: "))
            delete_task(index)
        elif choice == "4":
            print("Пока!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()