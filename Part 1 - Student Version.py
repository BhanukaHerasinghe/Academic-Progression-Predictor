# I declare that my work contains no examples of misconduct, such as plagiarism,or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student Id :  Uow - 18701098/1 ---- IIT Id - 20200468

# Date - 2021 - 12- 06



Pass  = 0
Defer = 0    # create variables
Fail  = 0
Total = 0

print("please input Credit Levels are 0, 20, 40, 60, 80, 100, 120 \n") # valid Credit Levels,give final output based on that

def process_of_result(Pass,Defer,Fail):
    if Pass == 120:
        print("progress")
    elif Pass == 100 and Defer == 20:
        print ("progress (module trailer)")         
    elif Pass == 100 and Fail == 20 :
        print ("progress (module trailer)")                 
    elif Pass == 80:
        print("Do not Progress - module retriever")
    elif Pass == 60:
        print("Do not Progress - module retriever")
    elif Pass == 40 and Defer != 0:                        # check out the user input and validate in Progression outcomes
        print("Do not Progress - module retriever")
    elif Pass == 40 and Defer == 0:
        print("Exclude")
    elif Pass == 20 and Defer >= 40:
        print("Do not Progress - module retriever")
    elif Pass == 20 and Defer <= 20:
        print("Exclude")
    elif Pass == 0 and Defer >= 60:
        print("Do not Progress - module retriever")
    elif Pass == 0 and Defer <= 40:
        print("Exclude")



def validationPass():   # Validating the given input by user and check is it a pass value
    global Pass
    
    while True:     #if pass credit  not in range not an integer this while create a loop untill user enter correct value
        try:
            Pass = int(input("Please enter student credit at pass: ")) # getting user input for pass credit
        except ValueError:
            print("Incorrect Input...!!! Please Input Integer...")    # error handling in user inputs,if pass credit not  an int this one happen
            continue
        else:
            if ((0 <= Pass <= 120) and (Pass % 20 == 0)) :          # checkout the credit Range given by user
                break
            else:
                print("Your input integer Out of range")   #
                
                      

def validationDefer():    # Validating the given input by user and check is it a Defer value
    global Defer
    
    while True:        #if Defer value not in range not an int this while create a loop untill user enter correct value
        try:
            Defer = int(input("Please enter student credit at defer: "))   # getting user input for Defer credit
        except ValueError:
            print("Incorrect Input...!!! Please Input Integer...")         # error handling in user inputs,if Defer credit not  an int this one happen
            continue
        else:
            if((0 <= Defer <= 120) and (Defer % 20 == 0)) :                # checkout the credit Range given by user
                break
            else:
                print("Your input integer Out of range")
                
             

def validationFail():   # Validating the given input by user and check is it a Fail value
    global Fail
    while True:       #if Fail value not in range not an int this while create a loop untill user enter correct value
        try:
            Fail = int(input("Please enter student credit at fail: "))    # getting user input for Fail credit
        except ValueError:
            print("Incorrect Input...!!! Please Input Integer...")        # error handling in user inputs,if Defer credit not  an int this one happen
            continue
        else:
            if((0 <= Fail <= 120) and (Fail % 20 == 0)):                 # checkout the credit Range given by user
                break
            else:
                print("Your input integer Out of range")
                
             

def validationTotal():    ##Get sum of pass, defer, fail and check sum is below or equals to 120
    global Total
    while True:
        Total = Pass + Defer + Fail            # getting the total credit mark in user inputs
        if Total != 120:
            print("Total incorrect")          # checkout the total credit mark given by user
            break
        else:
            process_of_result(Pass,Defer,Fail)
            break


validationPass()
validationDefer()   # call the function
validationFail()
validationTotal()


                


           
    
