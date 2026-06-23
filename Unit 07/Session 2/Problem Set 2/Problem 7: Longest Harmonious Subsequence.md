# Problem 7: Longest Harmonious Subsequence

You are composing a musical piece and have a sequence of notes represented by the string `notes`. Each note in the sequence can be either in a lower octave (lowercase letter) or higher octave (uppercase letter). A sequence of notes is considered harmonious if, for every note in the sequence, both its lower and higher octave versions are present.

For example, the phrase `"aAbB"` is harmonious because both `'a'` and `'A'` appear, as well as `'b'` and `'B'`. However, the phrase `"abA"` is not harmonious because `'b'` appears, but `'B'` does not.

Given a sequence of notes `notes`, use a divide and conquer approach to return the longest harmonious subsequence within `notes`. If there are multiple, return the one that appears first. If no harmonious sequence exists, return an empty string. 

```python
def longest_harmonious_subsequence(notes):
    pass
```

Example Usage:

```python
print(longest_harmonious_subsequence("GadaAg"))
print(longest_harmonious_subsequence("Bb"))
print(longest_harmonious_subsequence("c"))
```

Example Output:

```markdown
aAa
Example 1 Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, 
and both 'A' and 'a' appear. "aAa" is the longest nice substring.

Bb
Example 2 Explanation: "Bb" is a nice string because both 'B' and 'b' appear. 
The whole string is a substring.

Empty String
Example 3 Explanation: There are no nice substrings.
```
