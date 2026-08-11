def convert(value, from_unit, to_unit):
     if from_unit == "km":
         value_metr = value * 1000
     elif from_unit == "m":
         value_metr = value
     elif from_unit == "cm":
         value_metr = value/100
     else:
         print(f"Ошибка. Неизвестная единица")

     if to_unit == "km":
         result = value_metr/1000
     elif to_unit == "m":
         result = value_metr
     elif to_unit == "cm":
         result = value_metr * 100
     else:
        print(f"Ошибка. Неизвестная единица")
     return result
print(convert(5,"km", "m"))
print(convert(3,"m", "cm"))


