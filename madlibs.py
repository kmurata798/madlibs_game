#Stretch 1
wordlist = list()

def madlibs():
    
    """word = input("Type O for overview")

    if word == 'r' or word == 'R'
        for dList in wordlist:
            print(wordlist(dList))"""

    noun = input("Write a noun: ")
    wordlist.append(noun)
    
    verb = input("Write a verb: ")
    wordlist.append(verb)

    noun2 = input("Write another noun: ")
    wordlist.append(noun)

    adverb = input("Write an adverb: ")
    wordlist.append(adverb)

    adjective = input("Write a adjective: ")
    wordlist.append(adjective)
    
    verb2= input("Write another verb: ")
    wordlist.append(verb2)
                    
    adjective2 = input("Write another adjective: ")
    wordlist.append(adjective2)
    
    noun3 = input("Write one more noun: ")
    wordlist.append(noun3)
    
    animal = input("Write an animal: ")
    wordlist.append(animal)
    
    food = input("Write a food: ")
    wordlist.append(food)
    
    number = input("Write a number: ")
    wordlist.append(number)

    #Stretch 2 Color and Formatting
    print("\nOnce there was a little \033[0;31m {} \033[0m that would always \033[0;32m {} \033[0m next of a \033[1;33m {} \033[0m.\nThe weather was \033[0;31m {} \033[0m so there was a party where everyone had to \033[0;32m {} \033[0m until the party was over".format(noun, verb, noun2, adjective, verb2))
    print("There was all kinds of \033[1;33m {} \033[0m food at the party, but the \033[1;31m {} \033[0m was the most popular, everyone was eating that.".format(adjective2, food))
    print("Right before the party ended, a \033[0;31m {} \033[0m came down from the ceiling and sounded like a \033[0;34m {} \033[0m.\nIt sat down and had a drink, and all of a sudden \033[1;35m {} \033[0m more of those things joined the party and everyone danced all night!".format(noun3, animal, number))
    # RED \033[0;31m  GREEN = "\033[0;32m"  BLUE = "\033[0;34m"  PURPLE = "\033[0;35m"  YELLOW = "\033[1;33m"  LIGHT_RED = "\033[1;31m"  LIGHT_PURPLE = "\033[1;35m"  END = "\033[0m"

madlibs()
