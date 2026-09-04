"""Создайте класс History, который хранит список действий
пользователя: history = History([ "login", "open_profile",
"edit_profile", "logout" ])
Сделайте объект History итерируемым. При переборе
действия должны возвращаться по одному.
for action in history:
print(action)
Усложнение: Добавьте возможность создавать несколько
независимых итераций:
for action in history:
...
for action in history:
...
Обе итерации должны начинаться с первого элем"""
class HistoryIterator:
   def __init__(self,action):
       self.action = action
       self.index = 0
   def __iter__(self):
       return self
   def __next__(self):
       if self.index >=len(self.action):
           raise StopIteration
       action = self.action[self.index]
       self.index +=1
       return action

class History:
    def __init__(self,actions):
        self.actions = actions
    def __iter__(self):
        return HistoryIterator(self.actions)

history = History(["login", "open_profile", "edit_profile", "logout"])
print("Первая интерация:")
for action in history:
    print(action)

print("Вторая итерация:")
for action in history:
    print(action)




