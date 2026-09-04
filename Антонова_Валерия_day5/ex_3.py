from copy import deepcopy
hero ={
        "name":"Воин",
        "level":1,
        "inventory":["меч","щит"],
        "skills":{"attack":10, "defense":5}
      }
hero_1 = deepcopy(hero)
hero_2 = deepcopy(hero)
hero_3 = deepcopy(hero)
hero_1["name"] = "Рыцарь"
hero_2["inventory"].append("аптечка")
hero_3["skills"]["attack"] = 14
print(f"Исходный список:{hero}\nПервый герой:{hero_1}\nВторой герой:{hero_2}\nТретий герой:{hero_3}")