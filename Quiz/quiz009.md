# This is quiz 9

## Code solution
```.py
def shift_encryption(data:str,shift:int):
    data = data.strip().split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []

    for i in data:
        result.append("")
        for j in range(len(i)):
            result[data.index(i)] += alphabet[(shift%26)+(alphabet.index(i[j])-26)]

    return result

print(*shift_encryption("sentence to encrypt",5))
```

## Proof of work
![image](https://github.com/user-attachments/assets/face347c-7949-4526-b37f-b6ecdfbf2e2f)

## Flow chart
![image](https://github.com/user-attachments/assets/e2192a18-68aa-46e6-9a78-0bc71c2a8021)

## Paper solution
![20240929_143102](https://github.com/user-attachments/assets/4297552e-0c23-4629-bca5-ab25007fe05b)
