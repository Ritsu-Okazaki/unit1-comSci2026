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
