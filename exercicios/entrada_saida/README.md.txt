#Exercise 1: Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication

#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

Expected Output:

For example: print('Name', 'Is', 'James') will display Name**Is**James

#Exercise 3: Convert Decimal number to octal using print() output formatting
Given:

num = 8
Expected Output:

The octal number of decimal number 8 is 10

#Exercise 4: Display float number with 2 decimal places using print()
Given:

num = 458.541315
Expected Output:

458.54

#Exercise 5: Accept a list of 5 float numbers as an input from the user
Refer:

Take list as a input in Python.
Python list
Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]

#Exercise 6: Write all content of a given file into a new file by skipping line number 5
See:

Create a test.txt file and add the below content to it.

Given test.txt file:

line1
line2
line3
line4
line5
line6
line7
Expected Output: new_file.txt

line1
line2
line3
line4
line6
line7

#Exercise 7: Accept any three string from one input() call
Write a program to take three names as input from a user in the single input() function call.

#Home » Python Exercises » Python Input and Output Exercise
Python Input and Output Exercise
Updated on: September 6, 2021 | 85 Comments

In Python, we can use the input() to accept input from a user and print() to display output on the console. Also, we can use Python for file handling (Reading, writing, appending, and deleting files).

This Python Input and Output exercise aims to help Python developers to learn and practice the Python built-in functions print() and input() to perform input and output tasks. Also, we will solve exercises to practice file handling in Python.

Also Read:

Python input and Output
Pytohn File Handling
Python Input and Output Quiz
This Input and Output exercise includes the following: –

The exercise contains 10 questions and solutions provided for each question.
When you complete each question, you get more familiar with the Python Input and Output.
Let us know if you have any alternative solutions. It will help other developers.
Use Online Code Editor to solve exercise questions.

Table of contents
Exercise 1: Accept numbers from a user
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Exercise 3: Convert Decimal number to octal using print() output formatting
Exercise 4: Display float number with 2 decimal places using print()
Exercise 5: Accept a list of 5 float numbers as an input from the user
Exercise 6: Write all content of a given file into a new file by skipping line number 5
Exercise 7: Accept any three string from one input() call
Exercise 8: Format variables using a string.format() method.
Exercise 9: Check file is empty or not
Exercise 10: Read line number 4 from the following file
Exercise 1: Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication

Help: Take user input in Python

Show Hint
Show Solution
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

Expected Output:

For example: print('Name', 'Is', 'James') will display Name**Is**James

Show Hint
Show Solution
Exercise 3: Convert Decimal number to octal using print() output formatting
Given:

num = 8
Expected Output:

The octal number of decimal number 8 is 10

Show Hint
Show Solution
Exercise 4: Display float number with 2 decimal places using print()
Given:

num = 458.541315
Expected Output:

458.54
Show Hint
Show Solution
Exercise 5: Accept a list of 5 float numbers as an input from the user
Refer:

Take list as a input in Python.
Python list
Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]

Show Hint
Show Solution
numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)
 Run
Exercise 6: Write all content of a given file into a new file by skipping line number 5
See:

Python file handling
Python Read file
Python write file
Create a test.txt file and add the below content to it.

Given test.txt file:

line1
line2
line3
line4
line5
line6
line7
Expected Output: new_file.txt

line1
line2
line3
line4
line6
line7
Show Hint
Read all lines from a test.txt file using the readlines() method. This method returns all lines from a file as a list
Open new text file in write mode (w)
Set counter = 0
Iterate each line from a list
if the counter is 4, skip that line, else write that line in a new text file using the write() method
Increment counter by 1 in each iteration
Show Solution
# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1
Exercise 7: Accept any three string from one input() call
Write a program to take three names as input from a user in the single input() function call.

See: Get multiple inputs from a user in one line

Show Hint
Ask the user to enter three names separated by space
Split input string on whitespace using the split() function to get three individual names
Expected Output

Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly
Show Solution
str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)

#Exercise 8: Format variables using a string.format() method.

Write a program to use string.format() method to format the following three variables as per the expected output

Given:

totalMoney = 1000
quantity = 3
price = 450
Expected Output:

I have 1000 dollars so I can buy 3 football for 450.00 dollars.

#Exercise 9: Check file is empty or not
Write a program to check if the given file is empty or not

#Exercise 10: Read line number 4 from the following file
See:

Read Specific Lines From a File in Python
Python read file
Create a test.txt file and add the below content to it.

test.txt file:

line1
line2
line3
line4
line5
line6
line7