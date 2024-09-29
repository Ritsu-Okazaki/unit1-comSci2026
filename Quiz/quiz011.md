# This is quiz 11

## Code solution
```.py
def calender(month):
    offset_list = {1:0, 2:3, 3:4, 4:0, 5:2, 6:5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6}
    offset = offset_list[month]
    result = []
    days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10: 31, 11:30, 12:31}
    types = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    for i in range(offset, days[6]+offset):
        result.append(str(types[(i%7)])+" "+str(i-offset+1)+" ")
    print(*result)

calender(6)
```
