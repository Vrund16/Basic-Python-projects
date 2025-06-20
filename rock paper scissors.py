import random

choices=("r","p","s")    

while True:
    
     user_choice=input("Rock, Paper, or Scissors?(R/P/S): ").lower()
     if user_choice not in choices:
         print("Invalid choice!!!")
         continue
     machine_choice=random.choice(choices)

     print(f"You choose {user_choice} ")
     print(f"Computer choose {machine_choice} ")

     if user_choice==machine_choice:
         print("Game Tied !")

     elif user_choice=="r" and machine_choice=="s":
         print("You Win !!")
    
     elif user_choice=="r" and machine_choice=="p":
         print("You Lost !!")
    
     elif user_choice=="p" and machine_choice=="s":
         print("You Lost !!")    
    
     elif user_choice=="p" and machine_choice=="r":
         print("You Win !!") 
    
     elif user_choice=="s" and machine_choice=="r":
         print("You Lost !!")
    
     elif user_choice=="s" and machine_choice=="p":
         print("You Win !!")    
    
     want_to_continue=input("Do you want to Continue? (y/n) ").lower() 
     if want_to_continue=="n":
         break
    