# ----------------------------------------- IMPORTANT INFORTMATION -------------------------------------------------------
# In these practice problems, questions will be commented out by default. When you work on a problem, uncomment the relevant code
# by selecting the lines and pressing CTRL + / (Windows) or CMD + / (Mac). 
# For example, for problem 0, we select from PROBLEM 0 START to PROBLEM 0 END
# Try it below


# # ---------- PROBLEM 0 START ----------
# print('hello world! =)')
# # note the pretty colors!
# # ---------- PROBLEM 0 END ----------


# When you are finished with the problem, run it to make sure the output matches what you expect. Then, re-comment that problem 
# by using the same method and move on to the next problem! 


# ---------------------------------------- PROBLEM 1 START ----------------------------------------
# You are at the Apple store buying apples (what?).
# You want to know how much money you will spend if you buy a certain amount of apples. 
# Write code that takes in user input for the number of apples, converts it into an integer, 
# and calculates the total cost. 
# You MUST use variables to store the number of apples AND total cost.

# BONUS: format the print statement so that it prints out: 
# ___ apples costs $______.
# hint: You can't print integers and strings together. What CAN you print together? 

cost_apples = 0.4


# ----------------- SOLUTION GOES HERE --------------------
user_input = input("How many apples will you be buying? ")
total_cost = int(user_input) * cost_apples
print(user_input + " apples costs " + str(total_cost) + " dollars.")

# ---------------------------------------------------------

# ----------------------------------------PROBLEM 1 END ----------------------------------------

# ---------------------------------------- PROBLEM 2 START ----------------------------------------


grocery_list = ['apples', 'bananas', 'pineapples', 'flour', 'chives', 'milk', 'garlic']

# ---------- CODE GOES BELOW ---------- 

# 1. Print 'flour' by indexing the grocery list.
print(grocery_list[3])

# 2. Print 'milk'
print(grocery_list[5])

# 3. Print the first 5 items of the grocery list in 1 line. 
print(grocery_list[0:5])

# 4. Add "cheese" to the list.
grocery_list.append('cheese')
print(grocery_list)

# 5. Remove "pineapples" from the list.
grocery_list.remove('pineapples')
print(grocery_list)

# 6. Print the length of the list.
print(len(grocery_list))

# 7. Replace "bananas" with "cookies" in the list.
grocery_list[1] = 'cookies'
print(grocery_list)

# 8. Print the whole list. 
print(grocery_list)

# ---------------------------------------- PROBLEM 2 END ----------------------------------------

# ---------------------------------------- PROBLEM 3 START ----------------------------------------
# This is a challenge problem! In programming, swapping values is an important skill to have. 
# 

# Swap the values in variables a and b.
a = input("Type in a value for variable a: ")
b = input("Type in a value for variable b: ")

# ---------- SOLUTION GOES HERE ----------
temp = a
a = b
b = temp

# --------------------------------------- 

print('a is now: ', a)
print('b is now: ', b)

# ---------------------------------------- PROBLEM 3 END ----------------------------------------

# ---------------------------------------- PROBLEM 4 START ----------------------------------------

# Write code that will use the input() method to take information as prompted. Then combine them into a sentence using the template below and print. 
# TEMPLATE: 
# "Hello, my name is _____, and I am _____ year(s) old. I am a ______ major."
# Replace the blanks for name, age, and major respectively. 

# ---------- CODE GOES BELOW ----------
name = input('What is your name? ')
age = input('How old are you? ')
major = input('What are you majoring in? ')
print("Hello, my name is " + name + ", and I am " + age + " years old. I am a(n) " + major + " major.")
# ---------------------------------------- PROBLEM 4 END ----------------------------------------