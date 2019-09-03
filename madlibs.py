from colors import red, green, blue, yellow

#Stretch 1
wordlist = list()

def madlibs():
    
    """word = input("Type O for overview")

    if word == 'r' or word == 'R'
        for dList in wordlist:
            print(dList)"""

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

    
    print("\nOnce there was a little {} that would always {} next of a {}.\nThe weather was {} so there was a party where everyone had to {} until the party was over".format(red(noun), green(verb), red(noun2), yellow(adjective), green(verb2)))
    print("There was all kinds of {} food at the party, but the {} was the most popular, everyone was eating that.".format(yellow(adjective2), orange(food)))
    print("Right before the party ended, a {} came down from the ceiling and sounded like a {}.\nIt sat down and had a drink, and all of a sudden {} more of those things joined the party and everyone danced all night!".format(red(noun3), blue(animal), pink(number)))
    

madlibs()
