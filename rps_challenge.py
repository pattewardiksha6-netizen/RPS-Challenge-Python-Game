import random

Game Configuration

CHOICES = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
round_number = 0
total_rounds = 5

Welcome to rps chanllage

def display_welcome():
print("     🎮WELCOME TO RPS CHALLENGE🎮      ")
print("📌 Rules:")
print("   🪨 Rock beats Scissors")
print("   ✂️ Scissors beats Paper")
print("   📄 Paper beats Rock")
print("\n🏆 Match Type : Best of 5 Rounds")

User Input

def get_user_choice():
while True:

user = input("\n👉 Enter Rock, Paper, or Scissors: ").lower().strip()  

    if user in CHOICES:  
        return user  

    print("❌ Invalid input! Please enter a valid choice.")

Computer Choice

def get_computer_choice():

print("\n🤖 Computer is choosing...")  

return random.choice(CHOICES)

Winner Logic

def decide_winner(user, computer):

global user_score, computer_score  

if user == computer:  
    return "Tie"  

elif (  
    (user == "rock" and computer == "scissors") or  
    (user == "paper" and computer == "rock") or  
    (user == "scissors" and computer == "paper")  
):  

    user_score += 1  
    return "User"  

else:  

    computer_score += 1  
    return "Computer"

Scoreboard

def display_scoreboard():

print("📊 SCOREBOARD")  

print(f"👤 User Score: {user_score}")  
print(f"🤖 Computer Score : {computer_score}")

Final Result

def display_final_result():

print("FINAL RESULT")  

print(f"\n👤 Your Final Score      : {user_score}")  
print(f"🤖 Computer Final Score : {computer_score}")  

print("\n🎯 MATCH SUMMARY")  

if user_score > computer_score:  

    print("🎉 CONGRATULATIONS CHAMPION! 🎉")  
    print("🏆 You defeated the computer and won the match!")  
    print("🔥 Amazing gameplay! Keep it up!")  

elif computer_score > user_score:  

    print("🤖 COMPUTER WINS THE MATCH!")  
    print("😢 Better luck next time!")  
    print("💪 Don't give up — challenge again!")  

else:  

    print("🤝 IT'S A DRAW!")  
    print("⚔️ Both players gave a strong competition!")  
    print("🎮 What an exciting match!")  

print("\n" + "=" * 60)  
print("🙏 Thank You For Playing RPS Challenge!")  
print("🎮 Hope You Enjoyed The Game!")

Main Program

display_welcome()

while round_number < total_rounds:

round_number += 1  

print(f"\n🎯 Round {round_number} / {total_rounds}")  

# User Choice  
user_choice = get_user_choice()  

# Computer Choice  
computer_choice = get_computer_choice()  

print(f"\n👤 You Chose      : {user_choice.capitalize()}")  
print(f"🤖 Computer Chose : {computer_choice.capitalize()}")  

# Winner Decision  
winner = decide_winner(user_choice, computer_choice)  

# Result Display  
if winner == "Tie":  

    print("\n⚖️ It's a Tie!")  

elif winner == "User":  

    print("\n🎉 You Win This Round!")  

else:  

    print("\n😢 Computer Wins This Round!")  

# Scoreboard  
display_scoreboard()

Final Summary

display_final_result()
explain all one bye one how does it works basically if anyone asks question on this program the i can simply answer them any question
