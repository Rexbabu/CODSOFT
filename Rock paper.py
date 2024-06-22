import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_points=0
computer_points=0
while True:
    game=[rock,paper,scissors]
    user_choice=int(input("Choose one of these..TYPE..'0' for Rock.. '1' for Paper.. '2' for Scissors\n"))
    print("YOU'RE CHOICE>>")
    print(game[user_choice])
    print("COMPUTER CHOICE>>")
    computer_choice=random.randint(0,2)
    print(game[computer_choice])
    if user_choice>=3 or user_choice<0:
        print("It's Invalid Number, You Looser..!!")
    elif user_choice==0 and computer_choice==2:
        print("You Win..!!")
        user_points+=1
    elif computer_choice==0 and user_choice==2:
       print("You Lost..!!")
       computer_points+=1
    elif user_choice>computer_choice:
       print("You Win..!!")
       user_points+=1
    elif computer_choice>user_choice:
       print("You Lost..!!")
       computer_points+=1
    elif user_choice==computer_choice:
       print("It's a Draw..!")
    play_again=input("Do You Want To Play Again.. TYPE 'Y' for Yes..or 'N' for No\n").lower()
    if play_again!='y':
       break
print(f"YOU'RE POINTS ARE--{user_points}")

print(f"COMPUTER POINTS ARE--{computer_points}")

if user_points>computer_points:
   print(f"OVER WINNER IS--'YOU'")
else:
   print("OVER WINNER IS__'COMPUTER'")
