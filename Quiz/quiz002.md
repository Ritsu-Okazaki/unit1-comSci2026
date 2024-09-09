# This is quiz 2

## Code solution
```.py
def sum_check(tlist):
    if tlist[0] + tlist[1] == 20:
        return True
    else:
        return False

message = input()
input_numbers = message.split(", ")
temp_list = []

for i in input_numbers:
    temp_list.append(int(i))

print(sum_check(temp_list))
```

## Proof of work
![image](https://github.com/user-attachments/assets/8ed84178-580e-422d-82bb-96c73dcb8a3b)

## Paper work
