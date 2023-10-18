# 1. Конвертер оценок.
#Программа принимает на вход оценки по десятибалльной системе и
#присваивает одну из следующих оценок: “отлично”,
#“хорошо”, “удовлетворительно”, “неудовлетворительно”.
mark =int(input("введите оценку"))
if mark <= 2:
   print("неудовлетворительно")
elif mark == 3:
    print("удовлетворительно")
elif mark == 4:
    print("Хорошо")
elif mark == 5:
    print("отлично")

# 2. Возрастные группы
# Программа принимает на вход возраст пользователя и
# присваивает одну из возрастных групп: “ребенок”,
# “подросток”, “юноша / девушка”, “зрелый человек”,
# “пожилой человек”
age = int(input("Введите возраст: "))

if age <= 12:
    age_group = "ребенок"
elif age <= 18:
    age_group = "подросток"
elif age <= 30:
    age_group = "юноша / девушка"
elif age <= 60:
    age_group = "зрелый человек"
else:
    age_group = "пожилой человек"
print("Ваша возрастная группа:", age_group)

#3. Доброго времени суток
#Программа принимает на вход текущее время с помощью input
#и возвращает приветствие: “Доброе утро!”, “Добрый день!”,
#“Добрый вечер!”, “Доброй ночи!”

time = int(input("Введите текущее время (в часах): "))

if time >= 0 and time < 6:
    greeting = "Доброй ночи!"
elif time >= 6 and time < 12:
    greeting = "Доброе утро!"
elif time >= 12 and time < 18:
    greeting = "Добрый день!"
else:
    greeting = "Добрый вечер!"

print(greeting)

#4. Угадай число
#рограмма генерирует случайное число с помощью следующих строк:
#Напишите программу,
#которая помогает вам угадать сгенерированное число.
#В цикле while программа принимает на вход ваше число и сообщает:
#число больше сгенерированного или меньше сгенерированного.
#Цикл заканчивает работу, если вы угадали число.
#рограмма выводит на экран число.
#Усложните программу: добавьте счетчик ваших попыток угадать число.
import random

target_number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Угадайте число от 1 до 100: "))
    tries += 1

    if guess == target_number:
        print("Поздравляю, вы угадали число!")
        print("Число попыток:", tries)
        break
    elif guess < target_number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")