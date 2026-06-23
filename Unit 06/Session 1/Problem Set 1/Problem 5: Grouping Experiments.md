# Problem 5: Grouping Experiments

You have a list of experiment results for two types of experiments conducted in alternating order represented by a singly linked list. Each node in the list corresponds to an experiment result, and the position of the result in the 1-indexed sequence determines whether it is odd or even. 

Given the head of the linked list, `exp_results`, reorganize the experiment results so that all results in odd positions are grouped together first, followed by all results in even positions. The relative order of the results within the odd group and the even group must remain the same as the original sequence. The first result in the list is considered to be odd, the second result is even, and so on. Return the head of the reorganized list.

Your solution must have `O(1)` space complexity and `O(n)` time complexity.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
       print(current.value, end=" -> " if current.next else "\n")
       current = current.next

def odd_even_experiments(exp_results):
    pass
```

Example Usage:

*Example 1*
![Linked List experiment_results1 before and after grouping](https://courses.codepath.org/course_images/tip103/unit6_session1/grouping_experiments_ex1.jpg)

*Example 2*
![Linked List experiment_results2 before and after grouping](https://courses.codepath.org/course_images/tip103/unit6_session1/grouping_experiments_ex2.jpg)

```python
experiment_results1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
experiment_results2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

print_linked_lists(odd_even_experiments(experiment_results1))
print_linked_lists(odd_even_experiments(experiment_results2))
```

Example Output:

```markdown
1 -> 3 -> 5 -> 2 -> 4
2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```
