# This is quiz 8

## Code solution
```.py
from my_lib import validate_int

floor, room = 0, 0
all_rooms = []

for f in range(10):
    floor = f + 1
    for r in range(10):
        room = r + 1
        if len(str(room)) < 2:
            print(f"{floor}F0{room}")
            all_rooms.append(f"{floor}F0{room}")
        else:
            print(f"{floor}F{room}")
            all_rooms.append(f"{floor}F{room}")

room_num = validate_int(input("please enter the room number you want to locate: "))

if room_num is not None and room_num >= 1 and room_num <= 100:
    print(all_rooms[room_num - 1])
```

## Proof of work

![image](https://github.com/user-attachments/assets/951c9270-bdbb-4eab-93a4-bfcf007e43f6)


## Paper work

![quiz8SL](https://github.com/user-attachments/assets/0860499a-38e4-45ff-a57c-824e96cbb5c5)
