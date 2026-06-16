# Problem 4: Append Animals to Include Preference

You are managing an animal adoption center. You have:

-   A string`available`, representing the animals currently available for adoption.
-   A string`preferred`, representing a customer's preferred sequence of animals.

You want to make sure the`preferred`sequence appears as a**subsequence**of`available`. A subsequence means the characters appear in order, but not necessarily consecutively.

To achieve this, you are allowed to append characters to the**end**of`available`. You cannot remove characters or insert them elsewhere.

Return the**minimum number of characters**you need to append to the end of`available`so that`preferred`becomes a subsequence.

```
def append_animals(available, preferred):
  pass
```

Example Usage:

```
print(append_animals("catsdogs", "cows"))
print(append_animals("rabbit", "r"))
print(append_animals("fish", "bird"))
```

Example Output:

```
2
0
4
```

**Explanation:**

`available = "catsdogs"``preferred = "cows"`

-   `'c'`→ found at index 0
-   `'o'`→ found at index 5
-   `'w'`→ not present

You need to append`"ws"`to the end to complete the subsequence.**Minimum characters to append:**`2`

### Hint: Choosing the Right Approach
How do we know which data structure and/or algorithm to use when solving this problem? Should we use a stack? A queue? Two pointer? None of the above?

For this problem, two pointer would be a good choice because we're comparing and matching elements from two sequences in a linear fashion.

For more information about common use cases of stacks, queues, and two pointer, take a look at the unit cheatsheet.