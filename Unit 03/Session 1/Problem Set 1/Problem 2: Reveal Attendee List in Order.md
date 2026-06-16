# Problem 2: Reveal Attendee List in Order

You are planning a special event where each attendee has a unique registration number. These numbers are listed in the provided array `attendees`, but they are currently out of order.

At the event, attendees will walk on stage one by one following this special reveal process:

1.  The person at the **front of the line** walks on stage (this number is revealed).
2.  If there are still people left in line, the **next person** in front moves to the **back** of the line.
3.  Steps 1 and 2 repeat until everyone has walked on stage.

Your task is to**rearrange the `attendees` list*****before***the process starts so that the attendees walk on stage by registration number in**increasing order**.

Write a function `reveal_attendee_list_in_order(attendees)` that returns an array with the correct starting order, such that when the attendees follow the above reveal process they walk on stage from smallest registration number to largest registration number.

```
def reveal_attendee_list_in_order(attendees):
  pass
```

Example Usage:

```
print(reveal_attendee_list_in_order([17,13,11,2,3,5,7]))
print(reveal_attendee_list_in_order([1,1000]))
```

Example Output:

```
[2,13,3,11,5,17,7]
[1,1000]
```

### Example 1 Explanation
Suppose you reorder the `attendees` list to:

```
Start: [2, 13, 3, 11, 5, 17, 7]
```

Now apply the reveal process step-by-step:

| Step | Action | Line Left | Revealed So Far |
| --- | --- | --- | --- |
| 1 | Reveal 2 | \[13, 3, 11, 5, 17, 7\] | \[2\] |
| 2 | Move 13 to end | \[3, 11, 5, 17, 7, 13\] | \[2\] |
| 3 | Reveal 3 | \[11, 5, 17, 7, 13\] | \[2, 3\] |
| 4 | Move 11 to end | \[5, 17, 7, 13, 11\] | \[2, 3\] |
| 5 | Reveal 5 | \[17, 7, 13, 11\] | \[2, 3, 5\] |
| 6 | Move 17 to end | \[7, 13, 11, 17\] | \[2, 3, 5\] |
| 7 | Reveal 7 | \[13, 11, 17\] | \[2, 3, 5, 7\] |
| 8 | Move 13 to end | \[11, 17, 13\] | \[2, 3, 5, 7\] |
| 9 | Reveal 11 | \[17, 13\] | \[2, 3, 5, 7, 11\] |
| 10 | Move 17 to end | \[13, 17\] | \[2, 3, 5, 7, 11\] |
| 11 | Reveal 13 | \[17\] | \[2, 3, 5, 7, 11, 13\] |
| 12 | Reveal 17 | \[\] | \[2, 3, 5, 7, 11, 13, 17\] ✅ |

The reordered`attendees`list`[2, 3, 5, 7, 11, 13, 17]`that results in registration numbers being revealed in increasing order is what your function should return.

### AI Hint: Queues
*Key Skill: Use AI to explain code concepts*

This problem may benefit from the use of a **queue**, a data structure that follows the First In, First Out (FIFO) principle.

If you are unfamiliar with queues, you can check the [Unit 3 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/3#!cheatsheet) for a refresher, or you can learn about them using a generative AI tool, like this:

*"You're an expert computer science tutor. Please explain what a queue is in Python, and provide a simple code example of how to create one."*

After you get your answer, you can also ask follow up questions:

*"How is a queue different from a list or stack? Can you show me examples of each?"*