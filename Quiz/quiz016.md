# This is quiz 16

## Code solution
```.py
def get_l3tt3r(msg:str):
    conversion = {"a":"4", "A":"4", "E":"3", "e":"3", "I": "1", "i":"1", "O":"0", "o":"0", " ":"_"}
    result = ""

    for letter in range(len(msg)):
        if msg[letter] in conversion:
            result += conversion[msg[letter]]
        else:
            result += msg[letter]

    return result

print(get_l3tt3r("Why did I choose CS?"))
```

## Proof of work
![image](https://github.com/user-attachments/assets/3a86cd89-82be-4e3c-a149-0ff362a6b8c1)

## Flow diagram
![image](https://github.com/user-attachments/assets/48f8c1e4-0cde-49ce-9e60-565af241ad25)

## Paper work
![20240930_110039](https://github.com/user-attachments/assets/89937530-fe3b-46f4-8e2c-81bad99d9ca5)
