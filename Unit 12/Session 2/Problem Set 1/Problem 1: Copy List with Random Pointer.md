# Problem 1: Copy List with Random Pointer

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `None`.

Construct a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Given the `head` of the original linked list, return the head of the copied linked list.

```python
class Node:
    def __init__(self, val, next=None, random=None):
        self.value = val
        self.next = next
        self.random = random

# For testing, prints (value, random pointer value) for each node
def print_linked_list(head):
    current = head
    if not head:
        print("Empty List")
    while current:
        print((current.value, current.random.value), end=" -> " if current.next else "\n")
        current = current.next

# For testing, prints object ids for each node
def print_list_ids(head):
    current = head
    if not head:
        print("Empty List")
    while current:
        print(id(current), end=" -> " if current.next else "\n")
        current = current.next

def copy_random_list(head):
    pass
```

Example Usage 1:

![Example 1 Linked List with Random Pointers Shown](../../Unit%20Assets/copy_list_with_random_pointer_ex1.png)

```python
seven = Node(7)
thirteen = Node(13)
eleven = Node(11)
ten = Node(10)
one = Node(1)

seven.next = thirteen
thirteen.next = eleven
eleven.next = ten
ten.next = one

thirteen.random = seven
eleven.random = one
ten.random = eleven
one.random = seven

copied_list = copy_random_list(seven)
print_linked_list(copied_list)
print_list_ids(seven)
print_list_ids(copied_list)
```

Example Output 1:

```markdown
(7, None) -> (13, 7) -> (11, 1) -> (10, 11) -> (1, 7)
4341867088 -> 4341866992 -> 4341866848 -> 4341866704 -> 4341866608 
4341858208 -> 4341858064 -> 4341857968 -> 4341857872 -> 4341857776
Example 1 Explanation:
The node and random pointer values match that of the input list. The second two printed lists
which represent the object ids of each node are different from. Note that object ids will be different
each time you run your code and will likely differ from those shown above. The important thing is 
that the ids of the original list do not match the ids of the copied list. 
```

Example Usage 2:

![Example 2 Linked List with Random Pointers Shown](../../Unit%20Assets/copy_list_with_random_pointer_ex2.png)

```python
one = Node(1)
two = Node(2)

one.next = two

one.random = two
two.random = two

copied_list = copy_random_list(one)
print_linked_list(copied_list)
print_list_ids(one)
print_list_ids(copied_list)
```

Example Output 2:

```markdown
(1, 2) -> (2, 2)
4368363472 -> 4368363376
4368363232 -> 4368363088
```

Example Usage 3: 

![Example 3 Linked List with Random Pointers Shown](../../Unit%20Assets/copy_list_with_random_pointer_ex3.png)

```python
first = Node(3)
second = Node(3)
third = Node(3)

first.next = second
second.next = third

second.random = first

copied_list = copy_random_list(first)
print_linked_list(copied_list)
print_list_ids(first)
print_list_ids(copied_list)
```

Example Output 3: 

```markdown
(3, None) -> (3, 3) -> (3, None)
4375769040 -> 4375768944 -> 4375768800
4375768656 -> 4375768560 -> 4375768416
```

<details>
  <summary><strong>💡 Hint: Python Object IDs</strong></summary>

In Python, all objects you create, including `Node` objects, are assigned unique identifiers called **object IDs**. The ID is typically the memory address wehre the object is stored in your computer, and it stays constant during the object's lifetime.

 The `id()` function returns this unique ID for any given object, allowing you to check if two variables refer to the same object in memory. If two objects have the same ID, they are the same instance in memory, whereas different IDs indicate different objects.

The included `print_list_id()` function accepts the `head` of a linked list, and prints the object ID of every node in the list. If you have successfully made a deep copy of the list, then each node in both the original and copied list will have the exact same `value`, but their object IDs will be different.

</details>
