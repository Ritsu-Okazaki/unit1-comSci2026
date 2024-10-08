# This is quiz 10

## Code solution
```.py
def power_unit(number:int, unit:str):
    result = []
    units = {12: "Tera", 9:"Giga", 6:"Mega", 3:"Kilo", 0:"Unit", -3:"Mili", -6:"Micro", -9:"Nano", -12:"Pico"}
    for i in range(12, -15, -3):
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
            result.append("".join(temp2)+ " "*(30-len("".join(temp2))) + units[i] + " " + unit)
        else:
            temp = str(number*(10**i))
            for letter in range(len(temp), 0, -1):
                if letter % 3 == 0 and letter != len(temp):
                    temp2.append(" ")
                    temp2.append(temp[-letter])
                else:
                    temp2.append(temp[-letter])
            result.append("".join(temp2)+ " "*(30-len("".join(temp2))) + units[i] + " " + unit)

    for t in result:
        print(t)

power_unit(26,"gram")
```

## Proof of work
![image](https://github.com/user-attachments/assets/16bd3bb0-fa36-4278-bfc1-34931a870ee1)

## Flow diagram
![image](https://github.com/user-attachments/assets/9b557927-62a5-48e7-b6b7-f374e21864f3)

## Prior tests
```.py
num = 120000000

length = len(str(num))
space = []
result = ""

for i in range(length,0,-1):
    if i % 3 == 0:
        result += " "
        result += str(num)[-i]
    else:
        result += str(num)[-i]

print(result) # 120 000 000
```

## Paper work
![20240930_204701](https://github.com/user-attachments/assets/79cc0eaf-cdc3-4ecb-b261-0718cfc6f9ce)
