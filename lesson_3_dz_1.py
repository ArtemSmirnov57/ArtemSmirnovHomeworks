# Lesson 3 dz 1 Smirnov Artem
my_dictionary = {"zero": "ноль", "one": "один", "two": "два", "three": "три",
                 "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь",
                 "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate(word):
    return my_dictionary.get(word)


print(num_translate(input("Введите любое число на английском языке, от одного до десяти: ")))