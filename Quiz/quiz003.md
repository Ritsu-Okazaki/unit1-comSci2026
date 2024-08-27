# This is quiz 3
## Code solution
```.py
in_protein = input("please enter the protein in the DNA chain you want to translate: ")

translation = {"A": "T", "C": "G", "G": "C", "T": "A"}
out_protein = ""

if in_protein in "AGTA":
    for i in range(len(in_protein)):
        out_protein += translation[in_protein[i]]
    print(out_protein)
else:
    print("invalid input")
    exit()
```

## Paper work
![20240827_150612](https://github.com/user-attachments/assets/32efc874-118f-484b-979c-07f8953fca08)
