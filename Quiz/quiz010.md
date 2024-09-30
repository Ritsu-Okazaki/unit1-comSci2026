# This is quiz 10

## Code solution
```.py
def power_unit(number:int, unit:str):
    for i in range(-12, 12, 3):
        temp2 = []
        if i < 0:
            temp = str("{:.{}f}".format(number*(10**i), abs(i)))[2:]
            for letter in range(len(temp), 0, -1):
                if letter % 3 == 0:
                    temp2.append(" ")
                    temp2.append(temp[-letter])
                else:
                    temp2.append(temp[-letter])
            temp2.pop(0)
            temp2.insert(0,"0.")
        else:
            temp = str(number*(10**i))
            for letter in range(len(temp), 0, -1):
                if letter % 3 == 0 and letter != len(temp):
                    temp2.append(" ")
                    temp2.append(temp[-letter])
                else:
                    temp2.append(temp[-letter])
        print(temp, temp2)

power_unit(26,"gram")
```
