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
print(temp_list)
```

## Proof of work
![image](https://github.com/user-attachments/assets/573c7c1d-abaf-4921-a752-404eac0c70ec)

## Paper work
![20240827_150612](https://github.com/user-attachments/assets/32efc874-118f-484b-979c-07f8953fca08)
