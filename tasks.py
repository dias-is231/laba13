from storage import load_tasks, save_tasks

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список пуст")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Задача добавлена!")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Удалено: {removed}")
    else:
        print("Неверный номер!")