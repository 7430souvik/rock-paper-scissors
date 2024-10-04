


import random
rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper= '''
_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images= [rock,paper,scissors]

user_choice= int(input("what do you choose? 0 for rock, 1 for paper, 2 for scissors"))
print(game_images[user_choice])


computer_choice=random.randint(0,2)
print(game_images[computer_choice])


if  user_choice>=3 or user_choice<0:
    print("you typed  an invalid number")

elif user_choice==0 and computer_choice==2:
    print("you win!")

elif user_choice==2 and compter_choice==0:
    print("you lose!")

elif user_choice>computer_choice:
    print("you win!")

elif  computer_choice>user_choice:
    print("you lose!")

elif  computer_choice==user_choice:
    print("it's a draw!")


     

