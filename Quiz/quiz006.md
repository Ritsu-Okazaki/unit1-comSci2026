# This is quiz 6

## Code solution
```.py
from my_lib import validate_int, validate_boolean
import random

length, symbolYN = input("please enter the length for the password and decision if you want symbols in your password. [number], [True/False]").split(", ")

length = validate_int(length)
symbolYN = validate_boolean(symbolYN)

if length is None or symbolYN is None:
    exit("invalid input")

characters_withSymbol = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789%!"
characters_noSymbol = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
result = ""

if symbolYN is True:
    for i in range(length):
        result += characters_withSymbol[random.randint(0, 63)]
    print(result)
    exit()
else:
    for i in range(length):
        result += characters_withSymbol[random.randint(0, 61)]
    print(result)
    exit()
```

## Flow chart
![image](https://github.com/user-attachments/assets/c9441ba6-b8db-4a62-962b-fe183e73b20d)



## Proof of work

![image](https://github.com/user-attachments/assets/7b0d58bd-a15d-411a-8ff9-fe2dff9916e1)


## Paper work
![quiz5](https://github.com/user-attachments/assets/c662e9ee-bbc0-40ee-920e-e95430ea1589)

