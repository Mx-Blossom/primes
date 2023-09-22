#!/usr/bin/env python
# coding: utf-8

# In[34]:


primes = [1]
x = 2
num = 100

def check(a, b):
    one = 1
    templist = primes
    while a < len(templist):
        quotient = b/primes[a]
        check = int(quotient)
        if (check == quotient) and (quotient != one) and (quotient != b):
            print(b, " is divisible by ", primes[a]," and is not prime.")
            binary = 0
            break
        else:
            a = a+1
    if a < len(templist):
        binary = 0
        return binary
    else:
        binary = 1
        return binary

def addendum(c):
    primes.extend((c))

while x <= num:
    binary = check(0, x)
    if binary == 1:
        primes.extend([x])
        print(x, " is a prime number.")
        binary = 0
        x = x+1
    else:
        x=x+1
print(primes)


# In[ ]:




