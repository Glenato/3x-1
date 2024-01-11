import random
import fonctions

print ("Hi !\n")

print ("Welcome to the 3x + 1 program created by Glenato\n")

print ("""This program is based of the Collatz conjecture, here are the basic commands : 
- run + number : runs the 3x + 1 programme with the number you typed after 'run' 
- info : get more information about the 3x + 1 problème also called the Collatz conjecture\n""")

def syntaxe():
    print ("""This is the full syntaxe of the program :
- run + anynumber : runs the 3x + 1 programme with the number you typed after 'run'
- run random : runs the 3x + 1 programme with a random number from 1 to 1,000,000
- run forever : runs forever until you stop it or you find an other loop than 4, 2, 1
- output false : stops saving the output of the 3x + 1 programme in a txt file (thsi is True by default)
- graph false : stops showing a graph after the execution of the program 3x + 1
- info : get more information about the 3x + 1 program   
- customodd + '4x + 1' : changes the value added to the odd numbers to whatever is after customodd (here is : 4x + 1)
- customeven + '2' : changes the value added to the even numbers to whatever is after customeven (here is : 2)
""")
def info ():
    print ("""\n\nThe Collatz conjecture, also known as the 3n + 1 conjecture, is a mathematical sequence defined as follows:

1) Start with any positive integer n.
2) If n is even, divide it by 2 to get n/2.
3) If n is odd, multiply it by 3 and add 1 to get 3n + 1.
4) Repeat the process indefinitely, generating a sequence of numbers.

The conjecture proposes that, regardless of the starting value of n, the sequence will always eventually reach the number 1. Once the sequence reaches 1, it enters a cycle where subsequent values alternate between even and odd, continually reaching the cycle 4, 2, 1, 4, 2, 1, and so on.

While the Collatz conjecture is easy to state and understand, proving it for all positive integers remains an unsolved problem in mathematics. The behavior of the sequence is unpredictable, and it's not known whether every sequence eventually reaches 1, or if there exists a sequence that diverges to infinity. Despite its apparent simplicity, the Collatz conjecture has intrigued mathematicians since it was first introduced by Lothar Collatz in 1937.\n
For more detail you can always check this wikipedia article on the Collatz conjecture : \n\nhttps://en.wikipedia.org/wiki/Collatz_conjecture""")

while True:
    user_input = input("--> ")

    if user_input.lower().strip() =="info":
        info() 

    if user_input.lower()=="run random":
        random_number =random.randint(1,1000000000000000)
        print (random_number)
        reply, lilist = fonctions.formula(random_number)
        print (f"\nAfter having choosen {random_number} as a random number, this is a list with every number it encountered :\n\n{lilist}")
    
    elif "run forever" in user_input.lower():

        user_input = user_input.removeprefix("run forever").strip()
        
        if user_input.strip() == "":
            number = fonctions.run_forever()

        else:
            try: 
                user_input = int (user_input)
                if user_input <= 0:
                    print ("Your number must be an integer abouve the number 0")

                else:
                    number = fonctions.run_forever(user_input)

            except ValueError:
                print ("Invalide syntaxe please use valide numbers after the run command (Exemple : run forever 12000)")
        
        print ("\nYou solved the 3x + 1 probleme, with the number "+ str(number) +" !!!\n\nCongratulations !!!\n")

    elif "run" in user_input:

        user_input = user_input.removeprefix("run").strip()

        try: 
            user_input = int (user_input)
            reply, lilist = fonctions.formula(user_input) 
            print (f"\nAfter you have choosen {user_input}, this is a list with every number it encountered :\n\n{lilist}")           
            
            del reply, lilist

        except ValueError:
            print ("Invalide syntaxe please use valide numbers after the run command (Exemple : run 123)")
