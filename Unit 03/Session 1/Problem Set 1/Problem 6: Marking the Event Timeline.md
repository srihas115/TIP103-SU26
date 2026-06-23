# Problem 6: Marking the Event Timeline

You are organizing a large event, and you need to mark the timeline for a series of scheduled activities.

You are given two strings:

-   `event`: A short string representing an event name.
-   `timeline`: A longer string representing the full timeline for the event.

Initially, the timeline is empty and represented by a string `t` of the same length as `timeline`, where every character is `'?'`.

In one turn, you can "mark" the timeline by placing the `event` string over any valid position in `t` and copying its letters onto `t`. This replaces the corresponding `'?'` characters in `t`.

**Rules:**

-   You can only place `event` where it fully fits within `t`.
-   Each time you mark the timeline, the corresponding letters in `t` are updated.
-   Your goal is to perform a sequence of marks so that `t` becomes exactly equal to `timeline`.
-   You may use at most `10 * len(timeline)` marks.

Return a list of the starting indices where you placed the `event` string during each mark. If it is impossible to turn `t` into `timeline` following these rules, return an empty list.

```python
def mark_event_timeline(event, timeline):
  pass
```

Example Usage:

```python
print(mark_event_timeline("abc", "ababc"))
print(mark_event_timeline("abca", "aabcaca"))
```

Example Output:

```
[0, 2]
[3, 0, 1]
```

**Explanation**

For `"ababc"`:

-   Start with `t = "?????"`
-   Place `"abc"` at index `0` → `t = "abc??"`
-   Place `"abc"` at index `2` → `t = "ababc"` — timeline is complete.


### Hint: Pseudocode

1.  Start with the initial state of`t`(a string of`?`characters) and add it to the queue
    1.  Each element in the queue should be a tuple representing the current state of`t`and the list of indices where`event`has been placed
2.  Process the queue
    1.  Dequeue an element to get the current state of`t`
    2.  For each possible position, try to place`event`at that position
    3.  If placing`event`helps in moving closer to`timeline`, enqueue the new state of`t`along with the updated list of indices
    4.  If the current state matches`timeline`, return the list of indices
3.  If the queue is exhausted or the number of turns exceeds the limit, return an empty list