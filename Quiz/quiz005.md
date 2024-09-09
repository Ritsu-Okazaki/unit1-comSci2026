# This is quiz 5

## Code solution
```.py
from my_lib import validate_alphabet

message = validate_alphabet(input("please enter the message you want to calculate the sum of alphabetical order: "))
result = 0

loweralphabet_order = "abcdefghijklmnopqrstuvwxyz"
upperalphabet_order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if message is None:
    exit("invalid input")

for i in range(len(message)):
    if message[i] in loweralphabet_order:
        result += loweralphabet_order.index(message[i])+1
    elif message[i] in upperalphabet_order:
        result += upperalphabet_order.index(message[i])+1
    else:
        if message[i] != " ":
            exit("invalid input")
        result -= ord(" ")

print(result)
```

## Proof of work

![image](https://github.com/user-attachments/assets/91673dd6-1d9c-4dfc-96cd-b0383dbf9408)
