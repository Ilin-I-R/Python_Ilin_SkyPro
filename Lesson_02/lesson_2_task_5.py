def month_to_season(m):

    if m in [12, 1, 2]:
        return "Зима"
    elif m in [3, 4, 5]:
        return "Весна"
    elif m in [6, 7, 8]:
        return "Лето"
    elif m in [9, 10, 11]:
        return "Осень"
    else:
        return "Месяц должен быть от 1 до 12"


print(month_to_season(24))
