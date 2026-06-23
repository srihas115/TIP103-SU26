# Problem 3: Segmenting Protein Chains for Analysis

As a biochemist, you are analyzing a long protein chain represented by a singly linked list, where each node is an amino acid. For a specific experiment, you need to split this protein chain into `k` consecutive segments for separate analysis. Each segment should be as equal in length as possible, with no two segments differing in size by more than one amino acid.

The segments should appear in the same order as the original protein chain, and segments earlier in the list should have a size greater than or equal to those occurring later. If the protein chain cannot be evenly divided, some segments may be an empty list.

Write a function `split_protein_chain()` that takes the head of the linked list `protein` and an integer `k`, and returns an array of `k` segments.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def split_protein_chain(protein, k):
    pass
```

Example Usage:

```python
protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
    print_linked_list(part)
```

Example Output:

```markdown
Ala -> Gly -> Leu
Val -> Pro -> Ser
Thr -> Cys
Example 1 Explanation: The input list has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than later parts.

Ala
Gly
Leu
Val
Empty List
Example 2 Explanation: The input list has been split into consecutive parts with size difference at most 1.
Because k is one greater than the length of the input list, the last segment is an empty list.
```

<br>
