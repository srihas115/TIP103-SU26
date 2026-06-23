# Problem 7: Lingual Frequencies

As a time traveling linguist, you are analyzing texts written in an ancient script. However, some words in the text are illegible and can't be deciphered. Write a function`find_most_frequent_word()`that accepts a string`text`and a list of illegible words`illegibles`and returns the most frequent word in`text`that is not an illegible word.

```python
def find_most_frequent_word(text, illegibles):
    pass
```

Example Usage:

```python
paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1))

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2))
```

Example Output:

```
a

ball
Example 2 Explanation:
"hit" occurs 3 times, but it is an unknown word.
"ball" occurs twice (and no other word does), so it is the most frequent legible word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is illegible.
```

<details>
    <summary>Hint: Cleaning up the String</summary>
    What string methods does Python have that might be useful for removing punctuation, spaces, standardizing capitalization, etc.? Use a search engine or check out this[reference for common Python string methods](https://www.w3schools.com/python/python_ref_string.asp)to learn what helpful methods might already exist.
</details>