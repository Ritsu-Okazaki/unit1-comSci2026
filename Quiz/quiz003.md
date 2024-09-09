# This is quiz 3

## Code solution
```.py
in_protein = input("please enter the protein in the DNA chain you want to translate: ")

translation = {"A": "T", "C": "G", "G": "C", "T": "A"}
out_protein = ""

for i in range(len(in_protein)):
    if in_protein[i] in "AGTC":
        out_protein += translation[in_protein[i]]
    else:
        exit("invalid input")

print(out_protein)
```

## Proof of work
![image](https://github.com/user-attachments/assets/573c7c1d-abaf-4921-a752-404eac0c70ec)

## Paper work
![20240827_150612](https://github.com/user-attachments/assets/32efc874-118f-484b-979c-07f8953fca08)
