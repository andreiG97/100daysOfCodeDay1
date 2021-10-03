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

player = int(input('Please select an option 0 (rock), 1 (paper), 2 (scissors)'))

elements = [rock, paper, scissors]

computer = random.randint(0, 2)
print(f'{elements[player]}\n{elements[computer]}')
if player == computer:
    print('Tie')
if player == 0 and computer == 2:
    print('Player wins')
elif player == 0 and computer == 1:
    print('Computer wins')
if player == 1 and computer == 0:
    print('Player wins')
elif player < computer:
    print('Computer wins')
if player == 2 and computer == 1:
    print('Player wins')
elif player > computer:
    print('Computer wins')

