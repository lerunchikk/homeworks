from database import engine, Base
import crud

Base.metadata.create_all(engine)


def print_users():
    users = crud.get_all_users()
    if not users:
        print(" Пользователи не найдены.")
        return
    print("\n Список пользователей")
    for user in users:
        print(f"ID: {user.id} | Имя: {user.name} | Email: {user.email}")


def print_tasks(tasks):
    if not tasks:
        print(" Задачи не найдены.")
        return
    print("\n Список задач ")
    for task in tasks:
        print(f"ID: {task.id} | Статус: {task.status} | Название: {task.title} | Владелец ID: {task.user_id}")


def main_menu():
    while True:
        print(" ЗАДАЧИ")
        print("1. Создать пользователя")
        print("2. Показать всех пользователей")
        print("3. Создать задачу")
        print("4. Показать все задачи")
        print("5. Показать задачи пользователя")
        print("6. Изменить статус задачи")
        print("7. Удалить задачу")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            name = input("Введите имя пользователя: ")
            email = input("Введите email пользователя: ")
            crud.create_user(name, email)

        elif choice == "2":
            print_users()

        elif choice == "3":
            print_users()
            try:
                user_id = int(input("Введите ID пользователя: "))
                title = input("Введите название задачи: ")
                desc = input("Введите описание задачи: ")
                crud.create_task(user_id, title, desc if desc else None)
            except ValueError:
                print(" ID должен быть числом!")

        elif choice == "4":
            tasks = crud.get_all_tasks()
            print_tasks(tasks)

        elif choice == "5":
            print_users()
            try:
                user_id = int(input("Введите ID пользователя: "))
                tasks = crud.get_user_tasks(user_id)
                print_tasks(tasks)
            except ValueError:
                print(" ID должен быть числом!")

        elif choice == "6":
            tasks = crud.get_all_tasks()
            print_tasks(tasks)
            try:
                task_id = int(input("Введите ID задачи для изменения статуса: "))
                new_status = input("Введите новый статус (например, 'В работе' или 'Выполнено'): ")
                crud.update_task_status(task_id, new_status)
            except ValueError:
                print(" ID должен быть числом!")

        elif choice == "7":
            tasks = crud.get_all_tasks()
            print_tasks(tasks)
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                crud.delete_task(task_id)
            except ValueError:
                print(" ID должен быть числом!")

        elif choice == "0":
            print(" До свидания!")
            break

        else:
            print("⚠ Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main_menu()