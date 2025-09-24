#rock paper scissor
import random
import time
import sys

computer_choice = random.choice(["Rock", "Paper", "Scissors"])

def jump_text(text, repeat=3):
    positions = [0, 2, 1, 3, 2, 0]  #how much the text jumps
    for _ in range(repeat):
        for pos in positions:
            sys.stdout.write("\r" + " " * pos + text)
            sys.stdout.flush()
            time.sleep(0.2)
    print()

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



ascii_art = {
    "Rock": rock,
    "Paper": paper,
    "Scissors": scissors,
}

while True:
    user_input = input("Rock 🪨, Paper 📄, or Scissors ✂️?: ").strip().capitalize()
    if user_input in ["Rock", "Paper", "Scissors"]:
        break
    print("Enter either Rock, Paper, Scissors")


user_line = ascii_art[user_input].splitlines()
computer_lines = ascii_art[computer_choice].splitlines()

print("\nYou                                        vs.                                             Computer:\n")

#Print line by line, side by side
for u_line, c_line in zip(user_line, computer_lines):
    print(f"{u_line:<20}                                                             {c_line}")

if user_input == computer_choice:
    jump_text("                                     It's a tie!")
elif user_input == "Rock" and computer_choice == "Scissors":
    jump_text("                                     You win")
elif user_input == "Paper" and computer_choice == "Rock":
    jump_text("                                     You win")
elif user_input == "Scissors" and computer_choice == "Paper":
    jump_text("                                     You win")
elif user_input == "Rock" and computer_choice == "Paper":
    jump_text("                                     Computer wins")
elif user_input == "Paper" and computer_choice == "Scissors":
    jump_text("                                     Computer wins")
elif user_input == "Scissors" and computer_choice == "Rock":
    jump_text("                                     Computer wins")
else:
    jump_text("Invalid input")
