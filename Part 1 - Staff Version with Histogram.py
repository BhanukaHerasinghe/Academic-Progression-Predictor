# I declare that my work contains no examples of misconduct, such as plagiarism,or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student Id :  Uow - 18701098/1 ---- IIT Id - 20200468

# Date - 2021 - 12- 06


Pass  = 0
Defer = 0   # create variables
Fail  = 0
Total = 0

progress = []
trailer = []
retriever = []
exclude = []

print("please input Credit Levels are 0, 20, 40, 60, 80, 100, 120 \n")

def process_of_result(Pass,Defer,Fail): #check all requirement,give final output based on that  
    if Pass == 120:
        print("progress")
        progress.append(0)
    elif Pass == 100 and Defer == 20:
        print ("progress (module trailer)")
        trailer.append(0)
    elif Pass == 100 and Fail == 20 :
        print ("progress (module trailer)")
        trailer.append(0)
    elif Pass == 80:
        print("Do not Progress - module retriever")
        retriever.append(0)
    elif Pass == 60:
        print("Do not Progress - module retriever")    # check out the user input and validate in Progression outcomes
        retriever.append(0)
    elif Pass == 40 and Defer != 0:
        print("Do not Progress - module retriever")
        retriever.append(0)
    elif Pass == 40 and Defer == 0:
        print("Exclude")
        exclude.append(0)
    elif Pass == 20 and Defer >= 40:
        print("Do not Progress - module retriever")
        retriever.append(0)
    elif Pass == 20 and Defer <= 20:
        print("Exclude")
        exclude.append(0)
    elif Pass == 0 and Defer >= 60:
        print("Do not Progress - module retriever")
        retriever.append(0)
    elif Pass == 0 and Defer <= 40:
        print("Exclude")
        exclude.append(0)



def validationPass():    # Validating the given input by user and check is it a pass value
    global Pass
    
    while True:   #if pass credit  not in range not an integer this while create a loop untill user enter correct value
        try:
            Pass = int(input("Please enter student credit at pass: "))  # getting user input for pass credit
        except ValueError:
            print("Incorrect Input...!!! Please Input Integer...")      # error handling in user inputs,if pass credit not  an int this one happen
            continue
        else:
            if ((0 <= Pass <= 120) and (Pass % 20 == 0)) :              # checkout the credit Range given by user
                break
            else:
                print("Your input integer Out of range")
                
                      

def validationDefer():     # Validating the given input by user and check is it a Defer value
    global Defer
    
    while True:       #if Defer value not in range not an int this while create a loop untill user enter correct value
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
    while True:     #if Fail value not in range not an int this while create a loop untill user enter correct value
        try:
            Fail = int(input("Please enter student credit at fail: "))   # getting user input for Fail credit
        except ValueError:
            print("Incorrect Input...!!! Please Input Integer...")      # error handling in user inputs,if fail credit not  an int this one happen
            continue
        else:
            if((0 <= Fail <= 120) and (Fail % 20 == 0)):               # checkout the credit Range given by user
                break
            else:
                print("Your input integer Out of range")
                
             

def validationTotal():   ##Get sum of pass, defer, fail and check sum is below or equals to 120
    global Total
    while True:
        Total = Pass + Defer + Fail   # getting the total credit mark in user inputs
        if Total != 120:
            print("Total incorrect")  # checkout the total credit mark given by user
            break
        else:
            process_of_result(Pass,Defer,Fail)
            break

def staff_histogram():  # printing the Horizontal histogram  base on that
    print("\n")
    print("=" * 80)           # print "=" mark  
    print("Horizontal Histogram\n")
    print("Progress",len(progress), " :", "*" * len(progress))
    print("Trailer", len(trailer), "  :", "*" * len(trailer))           #according to the user input credit level printing the histrogram table with "=" mark
    print("Retriever",len(retriever),":", "*" * len(retriever))
    print("Excluded",len(exclude),  " :", "*" * len(exclude))
    total_outcomes =  len(progress) + len(trailer) + len(retriever) + len(exclude)
    print("\n")
    print(total_outcomes, "outcomes in total.")
    print("=" * 80)

def re_run():   # run again tha loop
    global End
    while True:
        print("\n")
        try:
            End = input("If you want to add another student credit record\n"
                        "Please Enter 'y' for yes or 'q' to quit and view outcomes: ")     # getting user inputs for run again the loop
        except ValueError:
            print("Your input is wrong...!!!! Please Enter 'y' or 'q'")  # error handling in user inputs
        else:
            if End == 'q':
                staff_histogram()
                break
                

            elif End == 'y':
                print("\n")
                validationPass()
                validationDefer()
                validationFail()
                validationTotal()
                

            else:
                print("Please Enter 'y' or 'q'")

validationPass()
validationDefer()
validationFail()    # call the function
validationTotal()
re_run()


                


           
    
