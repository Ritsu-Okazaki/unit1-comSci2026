# This is quiz 14

## Code solution
```.py
def door_game(num:int):
    doors = ["0"] * num

    for i in range(num):
        for j in range(num):
            if j % (i+1) == 0:
                if doors[j] == "0":
                    doors[j] = "1"
                else:
                    doors[j] = "0"

    result = 0

    for i in range(len(doors)):
        if doors[i] == "1":
            result += 1

    return result

print(door_game(5678))
```

## Proof of work
![image](https://github.com/user-attachments/assets/1a1b9348-7c9e-48e4-9411-61691fb1f464)

## Flow diagram
![image](https://github.com/user-attachments/assets/b8278a9b-33ee-41f9-9687-2f20f7e1219c)

## Paper work
![20240929_171339](https://github.com/user-attachments/assets/1c204a25-a7eb-4b32-ab88-3d886a659224)
