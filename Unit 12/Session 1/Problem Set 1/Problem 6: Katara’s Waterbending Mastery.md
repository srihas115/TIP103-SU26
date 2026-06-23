# Problem 6: Katara’s Waterbending Mastery

Katara is working on perfecting her waterbending techniques, starting from a basic form `form1` and needing to adapt it to a more advanced form `form2`. To master the advanced form, Katara can perform three types of operations:

- **Insert** a move
- **Delete** a move
- **Replace** a move with another

Write a function `waterbending_mastery()` that calculates the minimum number of operations Katara needs to convert `form1` to `form2`.

```python
def waterbending_mastery(form1, form2):
    pass
```

Example Usage:

```python
print(waterbending_mastery("tide", "wave"))
print(waterbending_mastery("intention", "execution"))
```

Example Output:

```markdown
3  
Example 1 Explanation:  
tide -> wide (replace 't' with 'w')  
wide -> wade (replace 'i' with 'a')  
wade -> wave (replace 'd' with 'v')

5  
Example 2 Explanation:  
intention -> inention (remove 't')  
inention -> enention (replace 'i' with 'e')  
enention -> exention (replace 'n' with 'x')  
exention -> exection (replace 'n' with 'c')  
exection -> execution (insert 'u')
```
