# This is quiz 8 SL

## Code solution
```.py
floor, room = 0, 0

for f in range(10):
    floor = f + 1
    for r in range(10):
        room = r + 1
        if len(str(room)) < 2:
            print(f"{floor}F0{room}")
        else:
            print(f"{floor}F{room}")
```

## Proof of work

![image](https://github.com/user-attachments/assets/7acf45bc-f10e-4652-9585-2d52cc63e16d)

## Paper work

![quiz8SL](https://github.com/user-attachments/assets/0860499a-38e4-45ff-a57c-824e96cbb5c5)
