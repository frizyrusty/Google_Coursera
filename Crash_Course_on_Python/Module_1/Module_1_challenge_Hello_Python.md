## Module 1 challenge: Hello Python!


**1. Once you have learned the basics of a programming language, how does this affect your ability to learn and use a second programming language?**

> It’s difficult to learn and use a second language.
>
> **It’s easier to learn and use a second language.**
>
> You should only code in one language.
>
> The syntax and semantics will be the same.

**Correct**


---


**2. What is a function?**

> A document describing a software project
>
> The beginning of a program defining who wrote it and why
>
> The task a program is written to accomplish
>
> **A reusable block of code that performs a specific task**

**Correct**


---


**3. What are some of the benefits of automation? Select all that apply.**

> More cost-effective for complex, seldom-done tasks
>
> **Consistency**
>
> Can accomplish creative tasks
>
> **Doesn’t get tired**

**Correct**


---


**4. What is the term for the set of rules for how statements are constructed in a programming language?**

> **Syntax**
>
> Grammar
>
> Format
>
> Semantics

**Correct**


---


**5. What is the program that reads and executes Python code by translating it to computer instructions called?**

> Linker
>
> Translator
>
> **Interpreter**
>
> Compiler

**Correct**


---


**6. Complete the code so that the string "I am writing Python code!" will print to the screen. Remember that syntax precision is important in programming languages. A missing capital letter, spelling error, or punctuation mark can produce errors.**

```python
# Replace the blanks with the correct code and syntax:
print("I am writing Python code!")

# Should print: I am writing Python code!
```

**Correct**


---


**7. What should be the output of the expression below?**

```python
print(12/(1+2)+2**2)
```

> **8.0**
> 
> 6.0
> 
> 15.0
> 
> 81.0

**Correct**


---

**8. In one year, if there are 365 days, with 24 hours in a day, , write a program to calculate the number of hours in a year. Print the result on the screen. Note: Your result should be in the format of just a number, not a sentence.**


```python
# Enter code here:
print(24*365)

# Should print 8760
```

**Correct**


---


**9. In a passcode where each digit of the passcode is independent of the other digits and each digit can be any numeral from 0 through 9, the total number of combinations is the number of possibilities for each digit raised to the power of the length of the passcode. So, for a 1-numeral passcode, there would be 10 possibilities; one for every numeral from 0 to 9.  For a 2-numeral passcode, each numeral is independent of the other, so there would be 10 times 10 possibilities.**


Using this information, use Python to calculate and print the number of possible passwords that can be formed with 3 numerals. 

**Note:** Your result should be in the number format, not a sentence.

```python
# Should print 1000
print(10**3)
```


**Correct**


---


**10. Consider this scenario about using Python to make calculations:**

On a college campus, there are 30 computers in each of the 20 computer labs that are spread across campus.  The computers have a life cycle where they are replaced every five  years. One-fifth of the computers are replaced each year. 

Fill in the blank to calculate the number of computers that are replaced each year by dividing the total computers by the replacement cycle. Note: Your result should be a number. 

```python
total_computers = 30*20
replacement_cycle = 5
computers_per_year = total_computers / replacement_cycle

print(computers_per_year) # Should print 120.0
```

**Correct**


---


**11. What is a computer program?**

> **Step-by-step instructions on how to complete a set of tasks, to be executed by a computer.**
> 
> The syntax and semantics of a programming language. 
> 
> The overview of what the computer will have to do to solve an automation problem. 
> 
> A file that gets printed by the Python interpreter. 

**Correct**

---

**12. Which of the following are true about programming languages? Select all that apply.**

> **Similar to human language, programming languages use syntax and semantics.**
> 
> **Programming languages are used to write computer programs and scripts.**
> 
> Programming languages is a synonym for pseudocode. 
> 
> **Some common programming languages include Python, Java, C, C++, C#, and R.**

**Correct**

---

**13. What is a property of Python that makes it easier to understand than some other programming languages?**

> You can use Python code in any other language.
>
> Python doesn’t have a defined syntax.
>
> **Code is similar to the English language.**
>
> Basic guidelines can be given and it will write the code.

**Correct**

---

**14. What should be the output of the expression below?**

```python
print((9-3)/(2*(1+2)))
```

> 0.28
> 
> 19.36
> 
> 49.0
> 
> **1.0**

**Correct**

---

**15. Assuming there are 60 minutes in an hour, write a program that calculates the number of minutes in a 24 hour day. Print the result on the screen. Note: Your result should be in the format of just a number, not a sentence.**

```python
# Enter code here:
minutes_day = 24 * 60

print(minutes_day)

# Should print 1440
```


**Correct**

---

**16. Fill in the blank to calculate how many sectors a given 16 GB (gigabyte) hard disk drive has. The given hard drive is divided into sectors of 512 bytes each. Divide the total bytes on the drive by the number of bytes in a sector to calculate how many sectors this drive has.  Your result should be a number. Note: To calculate the total bytes on the disk drive, multiply by multiples of 1024. In the code below,  you can calculate the "disk_size" of 16 GB by multiplying 16 by 1024 three times to go from bytes, to kilobytes, to megabytes, and finally to gigabytes.**

```python
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / 512

print(sector_amount) # Should print 33554432.0
```


**Correct**

---

**17. Use Python to calculate how many different passwords can be formed with 3 lower case English letters (excludes any character not found in the English alphabet).  For a 1 letter password, there would be 26 possibilities; one for every letter of the English alphabet.  For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities. Using this information, print the amount of possible passwords that can be formed with 3 letters.**

```python
# Enter code here:
alphabets = 26
pass = alphabets ** 3
print(alphabets)

# Should print 17576
```

**Correct**