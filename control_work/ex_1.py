import copy
class Warrior:
    def __init__(self):
        self._health = 30
        self.attack = 5

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            value = 0
        self._health = value

    @property
    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage):
        before = self._health
        self._health = max(0, self._health - damage)
        return before - self._health

    def attack_target(self, target):
        target.take_damage(self.attack)

    def __str__(self):
        return f"{self.__class__.__name__}, HP: {self.health}, ATK: {self.attack}"

    def __add__(self, other):
        new = copy.copy(self)
        new.health = self._health + other
        new.attack = self.attack + other
        return new

    def __mul__(self, other):
        new = copy.copy(self)
        new.health = self._health * other
        new.attack = self.attack * other
        return new


class Fighter(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Mage(Warrior):
    def __init__(self):
        super().__init__()
        self.magic = 6

    def take_damage(self, damage):
        reduced = max(0, damage - self.magic)
        return super().take_damage(reduced)

    def attack_target(self, target):
        if target.attack < self.magic:
            dmg = self.attack + self.magic
        else:
            dmg = self.attack
        target.take_damage(dmg)

    def __str__(self):
        return f"Mage, HP: {self.health}, ATK: {self.attack}, MAG: {self.magic}"


class Paladin(Warrior):
    def __init__(self):
        super().__init__()
        self._health = 50
        self._max_health = 50
        self.attack = 6

    @Warrior.health.setter
    def health(self, value):
        if value < 0:
            value = 0
        elif value > self._max_health:
            value = self._max_health
        self._health = value

    def attack_target(self, target):
        damage_dealt = target.take_damage(self.attack)
        heal = damage_dealt * 0.2
        self.health = self._health + heal


def fight(unit1, unit2):
    while unit1.is_alive and unit2.is_alive:
        unit1.attack_target(unit2)
        if not unit2.is_alive:
            return True
        unit2.attack_target(unit1)
        if not unit1.is_alive:
            return False
    return unit1.is_alive


class Army:
    def __init__(self):
        self._warriors = []

    def add_members(self, unit_class, count):
        for _ in range(count):
            self._warriors.append(unit_class())

    def __iter__(self):
        return iter(self._warriors)

    def __len__(self):
        return len(self._warriors)

    def __getitem__(self, index):
        return self._warriors[index]

    def __add__(self, other):
        new_army = Army()
        new_army._warriors = [w + other for w in self._warriors]
        return new_army

    def __mul__(self, other):
        new_army = Army()
        new_army._warriors = [w * other for w in self._warriors]
        return new_army

    @property
    def total_health(self):
        return sum(w.health for w in self._warriors)

    @property
    def total_attack(self):
        return sum(w.attack for w in self._warriors)

    @property
    def alive_members(self):
        return sum(1 for w in self._warriors if w.is_alive)


w = Warrior()
f = Fighter()
m = Mage()
p = Paladin()
print(w)
print(f)
print(m)
print(p)

print("\nДуэль")
f1, f2 = Fighter(), Fighter()
print(f"Победил unit1? {fight(f1, f2)}")

print("\nОператоры")
stronger = f + 3
print(f"Fighter + 3 : {stronger}")
doubled = m * 2
print(f"Mage * 2  : {doubled}")
print(f"Оригинал  : {m}")

print("\nАрмия")
army = Army()
army.add_members(Fighter, 3)
army.add_members(Mage, 2)
army.add_members(Paladin, 1)
print(f"Длина: {len(army)}")
for warrior in army:
    print(warrior)
print(f"Срез: {army[1:3]}")

stronger_army = army + 5
print(f"\nArmy + 5, первый: {stronger_army[0]}")

print("\nХарактеристики")
print(f"total_health:{army.total_health}")
print(f"total_attack:{army.total_attack}")
print(f"alive_members:{army.alive_members}")