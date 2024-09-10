# This is quiz 4

## Code solution
```.py
number = input("enter a positive integer you want to factorize")

result = []
sums = 0

for i in range(len(number)):
    if number[i] not in "0123456789":
        print("invalid input")
        exit()

number = int(number)

for i in range(1,  number+1):
    if number % i == 0:
        result.append(i)
        sums += i

if sums-number  == number:
    print(*result, True)
    exit()

print(*result, False)
```

## Flow chart
![image](https://github.com/user-attachments/assets/e22795ab-2fd1-4843-a8f8-975da05ce17f)


## Proof of work

![image](https://github.com/user-attachments/assets/0743e50a-3e93-4b0d-a623-1c3e1c58a219)

## Paper work

![20240828_091028](https://github.com/user-attachments/assets/43055d37-cdd3-4bac-bf4c-d8fb56369384)
