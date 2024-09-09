![image](https://github.com/user-attachments/assets/85ced8ac-fd68-4f98-9386-4b9cfa7c8a73)# This is quiz 2

## Code solution HL
```.py
from my_lib import validate_int

message = input()
result = False
group_f, group_r = message.split("] [")
input_numbers_f = group_f.replace("[", "").replace("]", "").replace(",", "").split(" ")
input_numbers_r = group_r.replace("[", "").replace("]", "").replace(",", "").split(" ")

for i in range(len(input_numbers_f)):
    if validate_int(input_numbers_f[i]) + validate_int(input_numbers_r[i]) == 20:
        result = True

print(result)
```

## Code solution SL
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

## Proof of work HL
![image](https://github.com/user-attachments/assets/621f5d43-bb86-4f8b-b234-89487c2b46fd)


## Proof of work SL
![image](https://github.com/user-attachments/assets/8ed84178-580e-422d-82bb-96c73dcb8a3b)

## Paper work

![quiz2](https://github.com/user-attachments/assets/cdd22a63-59cc-49cc-8980-7da8ce4d21c9)
