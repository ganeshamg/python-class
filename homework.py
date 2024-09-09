# Initialize an empty dictionary
bablu = {}

# Request inputs from the users
# bablu["name"] = input("inter your name: ")
# bablu["surname"] = input("inter your surname: ")
# bablu["age"] = input("inter your age: ")
# bablu["address"] = input("inter your address: ")
# bablu["education"] = input("inter your education: ")
# print(bablu)

# Asignment Table of 2
# for i in range(1, 11):
#     print(f"2 x {i} = {2*i}")
    
# Asignment Table of 3
# for i in range(1, 11):
#     print(f"5 x {i} = {5*i}")

# n = int(input("enter a number"))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")2,3,5

# for loop
# n = 5 # number of row
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# while loop
# n = 5 # number of row
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(j , end=" ")
#         j += 1
#         print()
#         if i == 3: # break after the third row
#             break
#         i += 1

# # accept a number from the user
# num = int(input("enter a number: "))
# # initialize sum to 0
# total_sum = 0
# # loop to calculate the sum of all numbers from 1 to the given number
# for i in range(1, num+1):
#     total_sum += i
# # print the results
# print(f"the sum of all numbers from 1 to {num} is {total_sum}")


# # first half of the pattern
# n = 5 # number of rows
# for i in range (n, 0, -1):
#     print('*' * i)

# # second half of the pattern
# for i in range(2, n+1):
#     print('*' * i)
    

# import random
# a = random.randrange(1,10)
# score = 100
# count = 1
# while score==200:
#     if(a%2==0):
#         print("hit")
#         score = score + 20
#     else:
#         print("miss")
#         score = score - 20
#     count = count + 1
# print()
# print(f high score reached in {count} times)


# Hit or Miss Game
import random

def hit_or_miss():
    # Computer selects a random number between 1 and 100
    target = random.randint(1, 100)
    attempts = 0
    score = 100  # Player starts with 100 points
    
    print("Welcome to the Hit or Miss game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    print("You start with 100 points. Each miss deducts 20 points, and a hit adds 20 points.")
    
    while True:
        # Player inputs their guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        # Check if the guess is correct
        if guess < target:
            score -= 20
            print(f"Miss! Your guess is too low. Current score: {score}")
        elif guess > target:
            score -= 20
            print(f"Miss! Your guess is too high. Current score: {score}")
        else:
            score += 20
            print(f"Hit! You've guessed the correct number {target} in {attempts} attempts.")
            print(f"Your final score is: {score}")
            break
        
        # Prevent negative scores
        if score <= 0:
            print("Game over! You've run out of points.")
            break

if __name__ == "__main__":
    hit_or_miss()
