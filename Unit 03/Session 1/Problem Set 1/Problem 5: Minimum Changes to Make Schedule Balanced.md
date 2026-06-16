# Problem 5: Minimum Changes to Make Schedule Balanced

You are organizing a series of events, and each event is represented by a parenthesis in the string `schedule`, where an opening parenthesis `(` represents the start of an event, and a closing parenthesis `)` represents the end of an event. A balanced schedule means every event that starts has a corresponding end.

However, due to some scheduling issues, the current `schedule` might not be balanced. In one move, you can insert either a start or an end at any position in the `schedule`.

Return the minimum number of moves required to make the `schedule` balanced.

```
def min_changes_to_make_balanced(schedule):
  pass
```

Example Usage:

```
print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("((("))
```

Example Output:

```
1
3
```

### Hint: Choosing the Right Approach

How do we know which data structure and/or algorithm to use when solving this problem? Should we use a stack? A queue? Two pointer? None of the above?

For this problem, a stack would be a good choice because we're checking for the 'balance' of pairs of symbols.

For more information about common use cases of stacks, queues, and two pointers, take a look at the unit cheatsheet.