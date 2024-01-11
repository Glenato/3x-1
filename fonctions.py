#sets variables

again=True
lilist = []
symbols=["+","-","*", "/"]

def formula (number, show_list=True):
    lilist = []
    #makes a list in with it stores all the numbers encountered
    #this loop continues until there is 2 times a same number in the lilist
    x =True

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

    return number, lilist

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
