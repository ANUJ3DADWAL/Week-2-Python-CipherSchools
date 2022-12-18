import random
Guessing_number=int(input("Enter Your Lucky Number in between 1 to 100: "))
Winning_Number=random.randint(1,100)
guessed=1
game_over=False
while not game_over:
    if Guessing_number==Winning_Number:
        print(f"Hurry! ,You Win! The Game and you Guessed in {guessed} times")
        game_over=True
    else:
        if Guessing_number<Winning_Number:
            print("Too Low")
            guessed+=1
            Guessing_number=int(input("Guess Again: "))
        else:
            print("Too High")
            guessed+=1
            Guessing_number=int(input("Guess Again: "))    

    




