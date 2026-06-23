# Problem 3: Arrange Event Attendees by Priority

You are organizing a large event and need to arrange the attendees based on their priority levels. You are given a 0-indexed list`attendees`, where each element represents the priority level of an attendee, and an integer`priority`that indicates a particular level of priority.

Your task is to rearrange the`attendees`list such that the following conditions are met:

1.  Every attendee with a priority less than the specified`priority`appears before every attendee with a priority greater than the specified`priority`.
2.  Every attendee with a`priority`equal to the specified priority appears between the attendees with lower and higher priorities.
3.  The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.

Return the`attendees`list after the rearrangement.

```python
def arrange_attendees_by_priority(attendees, priority):
  pass
```

Example Usage:

```python
print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10))
print(arrange_attendees_by_priority([-3,4,3,2], 2))
```

Example Output:

```
[9,5,3,10,10,12,14]
[-3,2,4,3]
```

### Hint: Two Pointer Variation
Knowing how to use the basic version of techniques like two pointer is great, but as we begin solving harder problems, we often need to modify them to work in new situations.

For this problem, try using a variation of the two pointer technique where you maintain two pointers as well as a third pointer/iterator `i` to maintain three sections of the array:

-   less than priority
-   equal to priority
-   greater than priority