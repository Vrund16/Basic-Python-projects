import random

Guess_number=random.randint(1, 100)

while True:
  try:
     Guess=int(input("Guess the number between 1 to 100: "))
     if Guess<Guess_number:
       print ("Too low!")
     
     elif Guess>Guess_number:
       print("Too high!")
     
     else:
       print("Congratulations you guessed it correctly")
       break
      
  except ValueError: 
     print("Please enter a valid number")
