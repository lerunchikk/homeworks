def business_card(name, surname, **kwargs):
    print("Результат")
    print("==========================")
    print(f"{name} {surname}")
    for key, value in sorted(kwargs.items()):
        print(f"{key}: {value}")

business_card(name = "Никита", surname= "Никитич", Age = 30, City = "Минск", Company = "Google", Email = "nikitich23@ghail.com")