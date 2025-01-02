## Module 2 challenge: Basic Python Syntax Assessment


**1. Complete the code to output the statement, “Diego’s favorite food is lasagna”. Remember that precise syntax must be used to receive credit.**

```python
name = 'Diego'
fav_food = 'lasagna'
print(name + "’s favorite food is " + fav_food)
```

**Correct**


---


**2. What’s the value of this Python expression: 7 < "number"?**

> True
>
> False
>
> **TypeError**
>
> 0

**Correct**


---


**3. What directly follows the elif keyword in an elif statement?**

> A function definition
>
> A logical operator
>
> A colon
>
> **A comparison**

**Correct**

---



**4. Consider the following scenario about using if-elif-else statements:**

Police patrol a specific stretch of dangerous highway and are very particular about speed limits.  The speed limit is 65 miles per hour. Cars going 85 miles per hour or more are given a “Reckless Driving” ticket. Cars going more than 65 miles per hour but less than 85 miles per hour are given a “Speeding” ticket.  Any cars going less than 65 are labeled “Safe” in the system.  
Fill in the blanks in this function so it returns the proper ticket type or label.

```python
def speeding_ticket(speed):
    if speed>=80:
        ticket = "Reckless Driving"
    elif speed>65:
        ticket = "Speeding"
    else:
        ticket = "Safe"
    return ticket

print(speeding_ticket(87)) # Should print Reckless Driving
print(speeding_ticket(66)) # Should print Speeding
print(speeding_ticket(65)) # Should print Safe
print(speeding_ticket(85)) # Should print Reckless Driving
print(speeding_ticket(35)) # Should print Safe
print(speeding_ticket(77)) # Should print Speeding
```


**Correct**

---

**5. In the following code, what would be the output?**

```python
test_num = 12
if test_num > 15:
    print(test_num / 4)
else:
    print(test_num + 3)

```


> 3
> 
> 12
> 
> 4
> 
> **15**

**Correct**

---

**6. Fill in the blanks to complete the function. The “identify_IP” function receives an “IP_address” as a string through the function’s parameters, then it should print a description of the IP address. Currently, the function should only support three IP addresses and return "unknown" for all other IPs.**

```python
def identify_IP(IP_address):
    if IP_address == "192.168.1.1":
        IP_description = "Network router"
    elif IP_address == "8.8.8.8" or IP_address == "8.8.4.4":
        IP_description = "Google DNS server"
    elif IP_address == "142.250.191.46":
        IP_description = "Google.com"
    else:
        IP_description = "unknown"
    return IP_description

print(identify_IP("8.8.4.4")) # Should print 'Google DNS server'
print(identify_IP("142.250.191.46")) # Should print 'Google.com'
print(identify_IP("192.168.1.1")) # Should print 'Network router'
print(identify_IP("8.8.8.8")) # Should print 'Google DNS server'
print(identify_IP("10.10.10.10")) # Should print 'unknown'
print(identify_IP("")) # Should Should print 'unknown'

```

**Correct**

---

**7. Can you calculate the output of this code?**

```python
def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))

```


**Answer:** 15
 
**Correct**

---

**8. Fill in the blanks to complete the function. The “return_nonnegative” function takes in two numbers and determines which number is larger.  Then, it subtracts the smaller number from the larger and returns the result. The result will always be greater than or equal to 0. Complete the body of the function so that it returns the correct result.**

```python
def return_nonnegative(first_num, second_num):
    if first_num > second_num:
        result = first_num - second_num
    else:
        result = second_num - first_num
    return result


print(return_nonnegative(5, 5)) # Should print 0
print(return_nonnegative(4, 5)) # Should print 1
print(return_nonnegative(5, 3)) # Should print 2
print(return_nonnegative(2, 5)) # Should print 3
print(return_nonnegative(5, 0)) # Should print 5
print(return_nonnegative(0, 5)) # Should print 5

```

**Correct**

---

**10. Code that is written so that it is readable and doesn’t conceal its intent is called what?**

> Obvious code
>
> **Self-documenting code**
>
> Maintainable code
>
> Intentional code

**Correct**


---

**11. What's the value of this Python expression: "big" > "small"?**

> True
>
> **False**
>
> big
>
> small

**Correct**


---


**12. What is the elif keyword used for?**

> To mark the end of the if statement
>
> **To handle more than two comparison cases**
>
> To replace the "or" clause in the if statement
>
> Nothing - it's a misspelling of the else-if keyword

**Correct**


---


**13. What are some of the benefits of good code style? Select all that apply.**

> Makes sure the author will refactor it later
>
> **Makes the intent of the code obvious**
>
> **Easier to maintain**
>
> Allows it to never have to be touched again

**Correct**