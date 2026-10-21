
# MINI NUMBER ART STUDIO

# PART 1: Number Staircase
print("===== NUMBER STAIRCASE =====")

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# PART 2: Star Square
print("\n===== STAR SQUARE =====")

size = int(input("Enter square size: "))

for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()


# PART 3: Reverse Number Triangle
print("\n===== REVERSE NUMBER TRIANGLE =====")

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# PART 4: Guess the Secret Number
print("\n===== GUESS THE NUMBER =====")

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess a number from 1 to 10: "))

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Correct! You won! 🎉")

print("Thanks for playing!")
