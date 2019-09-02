def madlibs():
    wordlist = list()
    animal = input("Write an animal: ")
    wordlist.append(animal)
    food = input("Write a food: ")
    wordlist.append(food)
    adjective = input("Write a adjective: ")
    wordlist.append(adjective)
    number = input("Write a number: ")
    wordlist.append(number)
    verb = input("Write a verb: ")
    wordlist.append(verb)
    noun = input("Write an input: ")
    wordlist.append(noun)

    print("You see a {} eating {} outside of your window. You open the window and snatch the food {} and eat it. After you finish, you say {} and take a nap.".format(animal, food, adjective, number))

madlibs()