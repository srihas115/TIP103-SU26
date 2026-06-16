# Problem 4: Rearrange Guests by Attendance and Absence

You are organizing an event, and you have a 0-indexed list`guests`of even length, where each element represents either an attendee (positive integers) or an absence (negative integers). The list contains an equal number of attendees and absences.

You should return the`guests`list rearranged to satisfy the following conditions:

1.  Every consecutive pair of elements must have opposite signs, indicating that each attendee is followed by an absence or vice versa.
2.  For all elements with the same sign, the order in which they appear in the original list must be preserved.
3.  The rearranged list must begin with an attendee (positive integer).

Return the rearranged list after organizing the guests according to the conditions.

```
def rearrange_guests(guests):
  pass
```

Example Usage:

```
print(rearrange_guests([3,1,-2,-5,2,-4]))
print(rearrange_guests([-1,1]))
```

Example Output:

```
[3,-2,1,-5,2,-4]
[1,-1]
```

