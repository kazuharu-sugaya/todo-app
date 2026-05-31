FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("タスクがありません")
        return

    print("\n--- タスク一覧 ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def edit_task(tasks):
    show_tasks(tasks)

    num = int(input("編集する番号: "))
    new_task = input("新しいタスク名: ")

    tasks[num - 1] = new_task

    save_tasks(tasks)

    print("編集しました")


tasks = load_tasks()

while True:
    print("\n1.追加")
    print("2.一覧")
    print("3.編集")
    print("4.削除")
    print("5.終了")

    choice = input("選択してください: ")

    if choice == "1":
        task = input("タスク名: ")
        tasks.append(task)
        save_tasks(tasks)

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        edit_task(tasks)

    elif choice == "4":
        show_tasks(tasks)
        num = int(input("削除する番号: "))
        tasks.pop(num - 1)
        save_tasks(tasks)

    elif choice == "5":
        print("終了します")
        break

    else:
        print("正しい番号を入力してください")