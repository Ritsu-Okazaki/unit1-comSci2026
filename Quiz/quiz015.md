# This is quiz 15

## Code solution
```.py
def averageLength(wordlist:list):
    temp = 0
    for i in wordlist:
        for j in range(len(i)):
            if i[j] != " ":
                temp += 1
    return round(temp/len(wordlist),2)

print(averageLength(["Peru", "France", "Nepal"]))
```

## Proof of work
![image](https://github.com/user-attachments/assets/844d3665-c86c-4729-b088-caf9bf21cc54)

## Flow chart
![image](https://github.com/user-attachments/assets/7dffdfd5-1e09-43c2-9dfa-5c1925d0eb5a)

## Paper solution
![20240929_174945](https://github.com/user-attachments/assets/e85b4ffe-a3ab-4b3f-85fb-e030a91b6453)
