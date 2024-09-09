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
