# Problem 6: Time to Complete Each Dream Design

As an architect, you are working on a series of imaginative designs for various dreamscapes. Each design takes a certain amount of time to complete, depending on the complexity of the elements involved. You want to know how many days it will take for each design to be ready for the next one to begin, assuming each subsequent design is more complex and thus takes more time to finish.

You are given an array `design_times` where each element represents the time in days needed to complete a particular design. For each design, determine the number of days you will have to wait until a more complex design (one that takes more days) is ready to begin. If no such design exists for a particular design, return `0` for that position.

Return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th design to start working on a more complex design. If there is no future design that is more complex, keep `answer[i] == 0` instead.

```python
def time_to_complete_dream_designs(design_times):
    pass
```

Example Usage:

```python
print(time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3]))
print(time_to_complete_dream_designs([2, 3, 1, 4]))
print(time_to_complete_dream_designs([5, 5, 5, 5]))
```

Example Output:

```
[1, 1, 3, 2, 1, 1, 0, 0]
[1, 2, 1, 0]
[0, 0, 0, 0]
```