import matplotlib.pyplot as plt
#sets variables

again=True
lilist = []
symbols=["+","-","*", "/"]

def print_chart(lilist, number, output=False):

    y=lilist
    
    plt.plot(y, marker ="o")

    # Add labels and title
    plt.xlabel('Iterations')
    plt.ylabel('Values')

    plt.title('Result of the Collatz conjecture after using the number ' + str(number))

    #save the plot as output.txt
    if output == True:
        print ("output has been saved")
        plt.savefig(fname="output.png", format="png", dpi=500)
    # Show the plot
    plt.show()

def formula (number, show_list = True, show_chart = False, output=False):
    lilist = []
    #makes a list in with it stores all the numbers encountered
    #this loop continues until there is 2 times a same number in the lilist
    x =True
    user_input = number

    while x == True:
        if show_list ==True:
            print (lilist)

        if number in lilist:
            x=False
        lilist.append(number)  

        #if number is even divide by 2 if it is odd do 3x+1    
        if number%2 ==0:
            number=int (number/2)

        else:
            number=3*number+1
    if show_chart == True:
        print_chart(lilist ,user_input, output)

    return number, lilist

def ask_custom():

    c=True
    d=True
    global user_choice_symbol_even
    global user_choice_num_even
    global user_choice_symbol_odd
    global user_choice_num_odd

    while c==True:
        try:
            user_choice_symbol_even = str(input ("Give a symbole to use if an even number is encountered : "))
            user_choice_num_even = str(input ("Give a number to use if an even number is encountered : "))
        
        except:
            print ("Invalide symbol or number")

    while d==True:
        try:
            user_choice_symbol_odd = str(input ("Give a symbole to use if an odd number is encountered : "))
            user_choice_num_odd = str(input ("Give a number to use if an odd number is encountered : : "))
        
        except:
            print ("Invalide symbol or number")

def custom_odd(number):

    global result
    global lilist
    if user_choice_symbol_odd in symbols:

        # Check the symbol and perform the operation
        if user_choice_symbol_odd == symbols[0]:
            result = int(number) + int(user_choice_num_odd)
        
        elif user_choice_symbol_odd == symbols[1]:
            result = int(number) - int(user_choice_num_odd)
        
        elif user_choice_symbol_odd == symbols[2]:
            result = int(number) * int(user_choice_num_odd)
        
        elif user_choice_symbol_odd == symbols[3]:
            result = int(number) / int(user_choice_num_odd)

        return result
    #if the symbole is not recognised an error is given back
    else : 
        print ("Error : Unsupported symbol")


def custom_even(number):

    global result

    if user_choice_symbol_even in symbols:
        # Check the symbol and perform the operation
        if user_choice_symbol_even == symbols[0]:
            result = int(number) + int(user_choice_num_even)
        
        elif user_choice_symbol_even == symbols[1]:
            result = int(number) - int(user_choice_num_even)
        
        elif user_choice_symbol_even == symbols[2]:
            result = int(number) * int(user_choice_num_even)
        
        elif user_choice_symbol_even == symbols[3]:
            result = int(number) / int(user_choice_num_even)

        return result
    #if the symbole is not recognised an error is given back
    else : 
        print ("Error : Unsupported symbol")
    

def custom (number):

    ask_custom()
    x = True

    while x == True:
        print (lilist)

        #if a number was already seen in a list it means it entered a loop and the program stops 
        if number in lilist:
            x = False
            print (lilist)

        #adds number to list
        lilist.append (number)

            #if number is even execute custom_even fuction
        if number%2 ==0:
            number = custom_even(number)

        #if number is odd execute custom_even fuction
        else:
            number = custom_odd(number)

    print ("number = "+str(number))

def run_forever (number=1):

    x=True

    while x == True: 
        _, result = formula(number, False)

        if 1 in result[-3:]:
            print ("The number is not : " + str(number))
            number = number + 1

        else:
            x=False

    return number
