# print("...rock...")
# print("...paper...")
# print("...scissors...")

# player1 = input("(enter Player 1's choice): ")
# player2 = input("(enter Player 2's choice): ")

# print("SHOOT!")

# ======BREAK BREAK======REPEAT======BREAK BREAK======OVER======

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")

print("BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n" + "BRING ON THE AIR HORNS" + "\n")

player2 = input("Player 2, make your move: ")

if player1 == "rock" and player2 == "scirockssors":
    print("Player 1 Wins")
if player1 == "scissors" and player2 == "paper":
    print("Player 1 Wins")
if player1 == "paper" and player2 == "rock":
    print("Player 1 Wins")
if player1 == "rock" and player2 == "paper":
    print("Player 2 Wins")
if player1 == "scissors" and player2 == "rock":
    print("Player 2 Wins")
if player1 == "paper" and player2 == "scissors":
    print("Player 2 Wins")
if player1 == player2:
    print("It is a tie!")

# ======BREAK BREAK======REPEAT======BREAK BREAK======OVER======

# Refactoring the Code!
