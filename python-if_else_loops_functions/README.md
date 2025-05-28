# Python - if/else, loops, functions

## General
- Why indentation is so important in Python
- How to use the if , if ... else statements
- How to use comments
- How to affect values to variables
- How to use the while and for loops 
- How to use the break and continues statements
- How to use else clauses on loops
- What does the pass statement do, and when to use it
- How to use range
- What is a function and how do you use functions
- What does return a function that does not use any return statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

## 0. Positive anything is better than negative nothing

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the `number` stored in the variable number is positive or negative.

- You can find the source code [here](/rltoken/aBRwd0uo_aZMPK2CBG1syg)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import` , `random`, `randint` do. Please do not touch this code
- The output of the program should be:
      -The number, followed by
          -if the number is greater than 0: `is positive`
          -if the number is 0: `is zero`
          -if the number is less than 0: `is negative`
      -followed by a new line

```
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-4 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
0 is zero
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-3 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-10 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
10 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-5 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
6 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
7 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
5 is positive
guillaume@ubuntu:~/$ 
```

### Repo:
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-if_else_loops_functions`
- File: `0-positive_or_negative.py`
  
---

## 1. The last digit

This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number .

- You can find the source code [here](/rltoken/UdohgX1ToNOVf4cAa3KJxA)
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import , random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
- 

```
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/$ 
```

### Repo:
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-if_else_loops_functions
- File: 1-last_digit.py
  
---

## 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- Use only one print function with string format
- Use only one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module


```
guillaume@ubuntu:~/$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/$
```

### Repo:
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-if_else_loops_functions
- File: 2-print_alphabet.py
  
---
