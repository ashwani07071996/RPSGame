import random

def R_P_S():
    print("\n===welcome to RPS game====\n")
    print("1.rock")
    print("2.paper")
    print("3.sciessior")
    
    
    Flag=True
    
    while(Flag):

        user=int(input("enetr make a choice\n")) 
        if user==1:
            print("you have  take rock")
        elif user==2:
            print("you have take paper")
        elif user ==3:
            print("you have take scissior")
        else:
            print("invalide input")
            R_P_S()
            
            
        comp=random.randint(1,3)
        if comp==1:
            print(" computer take rock")
        elif comp==2:
            print("computer take paper")
        else:
            print("computer take scissior")
        

        if user==comp:
            print(" drow")
        elif user==1 and comp==3:
            print("you won")
        elif user ==2 and comp==1:
            print(" you won")
        elif user ==3 and comp==2:
            print(" you won")
        else:
            print(" comp won")
        end_game=input(" do u want to quit press Q")
        if end_game== "Q" or end_game=="q":
            Flag=False
        
        
   
R_P_S()