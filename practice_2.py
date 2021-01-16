# ----------------------------------------- IMPORTANT INFORTMATION -------------------------------------------------------
# In these practice problems, questions will be commented out by default. When you work on a problem, uncomment the relevant code
# by selecting the lines and pressing CTRL + / (Windows) or CMD + / (Mac). 
# For example, for problem 0, we select from PROBLEM 0 START to PROBLEM 0 END
# Try it below


# # ---------- PROBLEM 0 START ----------
# print('hello world!')
# # ---------- PROBLEM 0 END ----------


# When you are finished with the problem, run it to make sure the output matches what you expect. Then, re-comment that problem 
# by using the same method and move on to the next problem! 



# # ---------------------------------------- PROBLEM 1 START ----------------------------------------
# # Set x to a value such that the output is false

# # ---------- SOLUTION GOES HERE ----------
# x = 
# # ----------------------------------------

# print(x > 5)

# # Set y to a value such that the output is true

# # ---------- SOLUTION GOES HERE ----------
# y = 
# # ----------------------------------------

# print(y or False)

# # Set z to a value such that the output is true. 

# # ---------- SOLUTION GOES HERE ----------
# x = 
# y = 
# z = 
# # ----------------------------------------

# print(z and (not x or not y))

# # ---------------------------------------- PROBLEM 1 END ----------------------------------------



# # ---------------------------------------- PROBLEM 2 START ----------------------------------------

# # Write code that takes age as an input, and outputs legal drinking eligibility (drinking age in the United States is 21 years).
# # Example input/output: 
# # 5
# # You are not old enough to drink!

# user_input = input("Welcome to Scotty's bar. How old are you? \n")

# # ---------- SOLUTION GOES HERE ----------

# # ----------------------------------------


# # hint: You'll have to typecast the input!
# # ---------------------------------------- PROBLEM 2 END ----------------------------------------



# # ---------------------------------------- PROBLEM 3 START ----------------------------------------

# # Using a for loop, print out each item in the given shopping list.

# mall_trip = ['iPhone', 'Yeezys', 'perfume', 'laptop', 'Nintendo Switch', 'jacket']

# # ---------- SOLUTION GOES HERE ----------

# # ----------------------------------------

# # Using a for loop, print out the first 3 items in mall_trip. Remember the range() method!

# # ---------- SOLUTION GOES HERE ----------

# # ----------------------------------------

# # ---------------------------------------- PROBLEM 3 END ----------------------------------------



# # ---------------------------------------- PROBLEM 4 START - CHALLENGE ----------------------------------------
# # We are going to be making a game, where the computer randomly chooses a number (that will be given) between 1 and 100.
# # You will then need to input a guess and print into the terminal whether the guess is correct, too high, or too low.
# # When the guess is correct, the game will end. 

# import random
# target = random.randint(1,100)

# # ---------- SOLUTION GOES HERE ----------
# while True:
#     guess = int(input("Guess a number between 1 and 100: "))

# # ----------------------------------------

# # Hint 1: Remember to use a break statement when needed
# # Hint 2: This will require a lot of conditional statements!
# # ---------------------------------------- PROBLEM 4 END ----------------------------------------

# # ---------------------------------------- PROBLEM 5 START ----------------------------------------
# # Write a function called add_five() that takes a number as an input and returns that number + 5. 

# x = int(input("Type in a number: "))

# # ---------- SOLUTION GOES HERE ----------

# # ----------------------------------------

# print(str(x) + " + 5 is " + str(add_five(x)))
# # ---------------------------------------- PROBLEM 5 END ----------------------------------------



# ---------------------------------------- PROBLEM 6 START - CHALLENGE ----------------------------------------
# The Fibonacci sequence is a sequence of numbers, where each number is the sum of the previous 2 numbers.
# For example, the first few numbers in the sequence are: 
# 1 1 2 3 5 8 13 21 34
# Write a function that takes in a number, and prints that many terms of the series. 
# For example: 
# print_fib(5) prints: 
# 1
# 1
# 2
# 3
# 5

# 

# ---------- SOLUTION GOES HERE ----------
def print_fib(n): 
    n1 = 1
    n2 = 1
    current_term = 0
    temp = 0
    if n <= 0:
        print("Enter a Positive Number")
    else:
        print("Fibonacci sequence up to", n, ":")
    while current_term < n:
        print("Current term: "+  str(current_term+1) + ": " + str(n1))
        

# ----------------------------------------

n = int(input("How many terms? "))

# ---------- SOLUTION GOES HERE ----------

# ----------------------------------------

# ---------------------------------------- PROBLEM 6 END ----------------------------------------
