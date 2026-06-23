# Problem 2: Two-Pointer Palindrome

Write a function `is_palindrome()` that takes in a string `s` as a parameter and returns `True` if the string is a palindrome and`False`otherwise. You may assume the string contains only lowercase alphabetic characters.

The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

```python
def is_palindrome(s):
    pass
```

Example Usage

```python
s = "madam"
is_palindrome(s)

s = "madamweb"
is_palindrome(s)
```

Example Output:

```
True
False
```

<details>
    <summary>💡Hint: While Loops</summary>
    This problem may benefit from a while loop! If you are unfamiliar with while loop syntax in Python, use your independent research skills or the Python Syntax section of the unit cheatsheet to learn more.
</details>
<details>
    <summary>💡Hint: Two Pointer Technique </summary>
    This problem may benefit from a algorithmic technique called the**two pointer approach**. Take a look at the unit cheatsheet for a more in-depth overview of how this technique works.
</details>