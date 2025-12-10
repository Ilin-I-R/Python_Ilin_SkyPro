# Как-то получить от пользователя оценку
rate_as_number = input("Оцените работу оператора от 1 до 5 :")
rate = int(rate_as_number)

# Проверить, что оценка от 1 до 5
if (rate < 1):
    rate = 1

if (rate > 5):
    rate = 5

print(rate)

# В зависимости от оценки предложить дать обратную связь
feedback = ''

if rate == 1:
    feedback = input("Расскажите, что нам улучшить :")
elif rate == 2:
    feedback = input("Расскажите, что вас смутило :")
elif rate == 3:
    feedback = input("Расскажите, как нам стать лучше :")
elif rate == 4:
    feedback = input("Расскажите, почему не 5 :")
else:
    feedback = input("Расскажите, за что похвалить оператора :")


print(feedback)
