# This is quiz 1

## Code solution
```.py
def converter(g):
    if len(g) <= 2:
        return g
    else:
        return g[0]+str(len(g)-2)+g[-1]

i = str(input())

si = i.split()
results = []

for k in si:
    results.append(converter(k))
    
print(*results)
```

## Flow chart
![image](https://github.com/user-attachments/assets/9c013773-0bc5-41a1-ad83-187a63d7d147)

## Proof of work
![image](https://github.com/user-attachments/assets/42c3d543-426b-46b2-8fe6-f99fd9509d0d)

## Paper solution
![quiz1](https://github.com/user-attachments/assets/0b5082be-32de-4fc8-a493-51019fee4159)
