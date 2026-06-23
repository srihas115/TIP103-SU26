# Problem 5: Assigning Unique Nicknames to Contestants

In a reality TV show, contestants are assigned unique nicknames. However, two contestants cannot have the same nickname. If a contestant requests a nickname that has already been taken, the show will add a suffix to the name in the form of`(k)`, where`k`is the smallest positive integer that makes the nickname unique.

You are given an array of strings`nicknames`representing the requested nicknames for the contestants. Return an array of strings where`result[i]`is the actual nickname assigned to the`i`th contestant.

```python
def assign_unique_nicknames(nicknames):
    pass
```

Example Usage:

```python
nicknames1 = ["Champ","Diva","Champ","Ace"]
print(assign_unique_nicknames(nicknames1))

nicknames2 = ["Ace","Ace","Ace","Maverick"]
print(assign_unique_nicknames(nicknames2))

nicknames3 = ["Star","Star","Star","Star","Star"]
print(assign_unique_nicknames(nicknames3))
```

Example Output:

```
["Champ","Diva","Champ(1)","Ace"]
["Ace","Ace(1)","Ace(2)","Maverick"]
["Star","Star(1)","Star(2)","Star(3)","Star(4)"]
```

