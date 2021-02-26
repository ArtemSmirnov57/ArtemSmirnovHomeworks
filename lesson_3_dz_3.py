# Lesson 3 dz 3 Smirnov Artem
def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = []
        if letter in names_dict:
            names_dict[letter].append(i)

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Анастасия", "Евгений", "Борис"))
