# This is the quiz 001

## Paper solution


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

### Exception

When period, comma or other symbols are used, they also count as characters

## Proof of work
