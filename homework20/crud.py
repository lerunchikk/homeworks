from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from database import SessionLocal
from models import User, Task
def create_user(name:str,email:str)->int|None:
    with SessionLocal() as session:
        try:
            new_user = User(name = name, email = email)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            print(f"Пользователь:{name} успешно создан")
            return new_user.id
        except IntegrityError:
            session.rollback()
            print(f"Ошибка.Пользователь с таким email уже существует")
            return None

def get_all_users():
    with SessionLocal() as session:
        stmt = select(User)
        return session.scalars(stmt).all()

def create_task(user_id:int,title:str,description:str|None,)->int|None:
    with SessionLocal() as session:
        user = session.get(User,user_id)
        if not user:
            print(f"Ошибка.Пользователь с таким ID не найден")
            return None
        new_task = Task(title = title,description = description,user_id = user_id)
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        print(f"Задача:{title} успешно создана")
        return new_task.id
def get_all_task():
    with SessionLocal() as session:
        stmt = select(Task)
        return session.scalars(stmt).all()
def get_user_task(user_id:int):
    with SessionLocal() as session:
        stmt = select(Task).where(Task.user_id == user_id)
        return session.scalars(stmt).all()
def update_task_status(task_id:int, new_status:str)->bool:
    with SessionLocal() as session:
        task = session.get(Task,task_id)
        if not task:
            print(f"Ошибка.Задача с таким id не найдена")
            return False
        task.status = new_status
        session.commit()
        print(f" Статус задачи ID {task_id} изменен на '{new_status}'")
        return True

def delete_task(task_id:int)->bool:
    with SessionLocal() as session:
        task = session.get(Task,task_id)
        if not task:
            print("Ошибка: Задача с таким ID не найдена.")
            return False
        session.delete(task)
        session.commit()
        print(f" Задача ID {task_id} успешно удалена")
        return True

