## Unit 5 Cheatsheet

Here’s a quick reference sheet for Unit 5. While not an exhaustive list, it highlights the key syntax and concepts you’ll use in this unit, plus a few optional ideas that may help with problem-solving. You’re still expected to know required material from earlier units.

Sections are labeled for clarity:

- ✅ In-Scope: May appear on the assessment
- 💡 Not In-Scope: Useful, but not required

General Concepts ✅ In-Scope

### Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that uses 'objects' and their interactions to build applications and computer programs. We can think of objects as virtual representations of real life object or data type. Python offers us many built-in objects or data types like integers (Python representation of a whole number), floats (Python representation of a decimal number), and strings (Python representation of a chunk of text), but the real magic of OOP is that it allows us to also create our own data types!



#### Classes

Classes are the mechanism through which we can design our own custom data types. A class is a blueprint for our new data type/object and defines the characteristics and functionality that every object of that class will have. Classes are comprised of two things:

- **properties** variables that describe *characteristics* of our object.
- **methods** functions that define *behaviors* of our object.

You can think of properties like adjectives that describe our object and methods like verbs that describe actions that our objects can take or that we can perform on our object.



#### Defining a Class

Let's look at an example of using a class to create a virtual representation of a dog. We can create a `Dog` class by representing a dog as a combination of its name, breed, and owner - these are the `Dog` class' properties.

```python
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
```



#### Instantiating a Class

The `__init__()` function, also called the *constructor* describes how to build a new object or *instance* of a class. The job of the constructor is to assign values to object properties. Like a normal function, constructors can have parameters. The `Dog` constructor above takes in three arguments: the `name` of the dog we are creating, the `breed` of the dog, and the `owner` of the dog and assigns the argument values to the class properties of the same name.

The constructor (and all class methods) includes a special parameter `self`, which refers to the current instance of the class that is being created. We do not need to pass in a value for self when we call the constructor.

We call constructors differently than we call normal functions. Instead of calling the constructor by writing its function name `__init__()`, we call it by using the name of the class. For example, we can create a new `Dog` object/instance with the following:

```python
my_dog = Dog('Fido', 'Cocker Spaniel', 'Ada Lovelace')
```

The above code creates a dog whose name is `'Fido'`, breed is `'Cocker Spaniel'` and owner is `'Ada Lovelace'`.



#### Class Properties

We can access properties of an object using dot notation: `object_name.property_name`.

```python
print(my_dog.name) # Prints Fido
```

In the above example, we stored our Dog instance in the variable `my_dog`, so `my_dog` is the name of our object. The property we're interested in printing is the dog's name so we place `name` after `my_dog` separated with a `.`.



#### Class Methods

Methods are just functions attached to objects. We can define a method by using the same syntax we use to define a function, but indenting it inside of a class definition. All methods take in the parameter `self`, referring to the current instance of the class.

```python
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def call_dog(self):
        print(f"Here {self.name}!")
```

We can call a class method using the same dot notation we do for properties: `object_name.method_name()`.

```text
my_dog.call_dog() # Prints 'Here Fido!'
```

Methods can take parameters in addition to self.

```python
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def call_dog(self):
        print(f"Here {self.name}!")

    def command_trick(self, trick):
        print(f"{self.name}, {trick}!")
```

These parameters need to be passed arguments as we would with a normal function.

```text
my_dog.command_trick("roll over") # Prints 'Fido, roll over!'
```



### Linked Lists

#### Linked Lists vs Arrays

At a surface level, linked lists and Python lists are equivalent. They both allow us to store multiple items of any data type together as an ordered collection of data.

Linked lists and normal lists differ in how they store each item they contain within memory.

Normal Python lists store each consecutive element in an array. For example, say we have the list `['U', 'B', 'F', 'D', 'A', 'E']` with element `'U'` stored at memory location 200. Elements `'B'` through `'E'` would be stored at memory locations 201 through 205 respectively.

![UBFDAE list with memory location and indices show](Unit%20Assets/list_in_memory.png)

In contrast, each element of a linked list can be stored in non-related memory locations. The first item in a linked list might be stored at memory location 200, and the second item might be stored at memory location 512.

So that we can find each element of the list, each item in the list not only stores the data it wants to hold like `'U'` or `'B'`, but also a reference to where the next item in the list is stored in memory.

![UBFDAE as a linked list with memory location and indices show](Unit%20Assets/linked_list_in_memory.png)

The reason both lists and linked lists exist, is because linked lists have a lower time and space complexity for certain operations. Follow your curiosity and do some independent research if you'd like to explore this more!



#### Defining a Linked List

Linked lists are not a built-in data type in Python, therefore we must define a class to build a linked list.

Each element of a linked list is called a *node*. A node consists of a *value* equivalent to an element's value in a normal list, as well as a *pointer* or reference variable to the next node in the list.

![Node with value 42 and None as value of next reference](Unit%20Assets/linked_list_in_memory.png)

A `Node` class might commonly look like the following.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```

The `next` property is the pointer to the next node in the list. `next` is either another `Node` instance or `None` meaning there is no node after the current node. By default, `next` is `None`.

In technical interviewing scenarios, it is likely that you will only be provided with a `Node` class, and a variable containing the first node in the linked list (also called the head of the list).

In some scenarios, you may also be given a linked list class that includes a reference to the `head` of the list as an attribute and operations commonly performed on a list, such as appending a new node, as methods.

```python

class LinkedList:
    # Constructor.
    def __init__(self):
        # The first node in the linked list.
        # The head is either a Node object or None if the list is empty.
        self.head = None

    # Method. Adds a new node with the specific data value to the beginning of the linked list.
    def add_first(self, value):
        pass

    # Method. Adds a node with specified value to the end of the list.
    def append(self, value):
        pass

    # Method. Returns the length of the list.
    def length(self):
        pass

    # Method. Returns the value at a given index in the linked list.
    # Index count starts at 0.
    # Returns None if there are fewer nodes in the linked list than the index value.
    def get_at_index(self, index):
        pass
```



#### Linked List Traversal

Most interviewing problems involving linked list, will require you to traverse a linked list. Traversing a linked list means sequentially accessing each element of the list, starting with the first (head) node.

To perform a traversal, take the following steps:

1.  Create a pointer `current` and initialize it to the first node in the list.
2.  Create a while loop that continues iterating as long as the `current` node is not `None` (aka as long as there are still nodes in the list we haven't traversed).
3.  In the body of the while loop:
    - perform whatever actions you would like to the current node (e.g. printing the current node's value)
    - update `current` to point at the next node in the linked list

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def traverse(head):
        current = head
        while current:
            # Perform operations on the current node (e.g., print the value)
            current = current.next # Move to the next node
```





Advanced Concepts ✅ In-Scope

### Multiple Pass Technique

Sometimes a linked list must be traversed multiple times in order to solve a problem. This is common when we need to extract some information about the list before we begin manipulating it. For example, there are many problems that require us to know the length of a linked list in order to solve the overall problem.

Example Usage:

The following function returns the values of a linked list as pairs in a list of tuples. If the linked list has an odd length, the values cannot be evenly paired and the function returns `None`.

```text
Example Input List: 1->2->3->4
Example Input: head = 1
Expected Return Value: [(1, 2), (3, 4)]

Example Input List: 1->2->3
Example Input: head = 1
Expected Return Value: None
```

```python
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def pair_nodes(head):
    # Check if the list is empty
    if not head:
        return None

    # Pass 1: Get the length of the list
    current = head
    length = 0
    while current:
        length += 1
        current = current.next

    # If the length is odd, return None
    if length % 2 != 0:
        return None

    # Pass 2: If the length is even, create tuples of pairs
    pairs = []
    current = head
    while current:
        # Since we know the list length is even, current.next should always be valid here
        pairs.append((current.value, current.next.value))
        current = current.next.next  # Move to the next pair

    return pairs
```

Because we perform a constant number of traversals and each traversal is done in series, the time complexity of a function is not affected by conducting multiple consecutive passes over the list. If the length of our input list is `n`, the above function `pair_nodes()` performs `O(n + n)` operations which reduces to `O(2n)` which can be further reduced to `O(n)` operations.

Variations of this technique may also nest loops or extract certain traversals into helper functions. For example, we can rewrite our `pair_nodes()` function so that getting the length of the list is encapsulated in a helper function.

```python
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

# Helper function: Returns the length of the list
def get_length(head):

    # Pass 1: Get the length of the list
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    return length

def pair_nodes(head):
    # Check if the list is empty
    if not head:
        return None

    # If the length is odd, return None
    if get_length(head) % 2 != 0: # Call helper function
        return None

    # Pass 2: If the length is even, create tuples of pairs
    pairs = []
    current = head
    while current:
        # Since we know the list length is even, current.next should always be valid here
        pairs.append((current.value, current.next.value))
        current = current.next.next  # Move to the next pair

    return pairs
```

### Temporary Head Technique

When we solve linked list problems, we often encounter edge cases that involve the head of a linked list. Common edge cases involving the head of a linked list include:

- Deleting the current head of a linked list
- Adding a new element to the front of a linked list
- Reducing a linked list containing only one node to an empty list
- Adding a new node to an empty list

A common technique for handling these edge cases is creating a temporary head node. To apply this technique, an extra node object is created to serve as the temporary head of the list. We can use the temporary head as a placeholder that allows us to easily add items to an empty linked list or manipulate the actual head of a list as if it were any other node.

Example Usage:

The following function accepts the head of a linked list and a value and deletes the first node in the list with the specified value. It returns the head of the modified list.

```text
Example Input List: 1->2->4
Example Input: head = 1, val = 2
Expected Return Value: 1
Expected Return List: 1->4
```

```python
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def delete_node(head, val):
    temp_head = Node("temp") # Initialize a temporary head node
    temp_head.next = head    # Point the temporary head at the input list

    # Traverse the list
    previous = temp_head
    current = head
    while current:
        if current.value == val:          # If the current node is the node to delete
            previous.next = current.next  # Delete the node
            break                         # Break out of the loop

        previous = current
        current = current.next
    return temp_head.next # Return the head of the input list
```

Because we created a temporary head, deleting the head of the list can be handled in the same way that deleting any other element in the list is handled. We can also proceed directly to traversing the list without checking if `head` is `None`, because the existence of the temporary head means there is at least one node int he list.

\[=\] **Deleting a node without a temporary head**

We can still remove a node from a list without the use of a temporary head, but we need to handle edge cases individually.

```python
def delete_node(head, val):
    # Edge case 1: If the list is empty
    if not head:
        return head

    # Edge case 2: If the head node needs to be removed
    if head.value == val:
        return head.next

    # Now handle the general case
    previous = None
    current = head
    while current:
        if current.value == val:
            previous.next = current.next
            return head  # Return the head of the list after removal
        previous = current
        current = current.next

    return head  # Return the head if no node was removed
```

\[=\] **⚠️ Temp Node Terminology**

When conducting your own independent research into this technique, you may see the "temp head" technique referred to as the "dummy head" technique. Historically, “dumb” was used as a reference to a member of the deaf community and has negative connotations as a derogatory term. For this reason, CodePath refers to this technique as the "temp head" technique.

**Words Matter**. We want to call out these terms to increase awareness and ensure that we are inclusive in our communities. If you notice other words or behaviors that are not inclusive, please let a CodePath team member know or email <report@codepath.org>.

Check out these resources to learn more:

- [ACM on Words Matter](https://www.acm.org/diversity-inclusion/words-matter)
- [Lee & Low on the term "Dummy"](https://blog.leeandlow.com/2012/08/16/when-did-the-word-dummy-become-derogatory/)



### Slow-Fast Pointer Technique

The slow-fast pointer technique, also called the tortoise and hare algorithm, is a common technique used to solve linked list and other data structure problems that involve cyclic structures. It involves using two pointers that move at different speeds to solve problems such as cycle detection, finding the middle of a list, or determining the meeting point within a cycle.

To apply the technique, create two pointers:

1.  **Slow Pointer**: Increment one step at a time.
2.  **Fast Pointer**: Increment two steps at a time.

Example Usage:

The following function returns `True` if a linked list has a cycle and `False` otherwise.

```python
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def has_cycle(head):
    if not head:
        return False

    slow = head  # Starts at the head
    fast = head  # Also starts at the head

    while fast and fast.next:
        slow = slow.next          # Move slow pointer by one
        fast = fast.next.next     # Move fast pointer by two

        if slow == fast:          # If they meet, there's a cycle
            return True

    return False  # If fast reaches the end, no cycle
```

Think about this algorithm as if you had a walker and a runner moving around a track. If the walker and runner start at the same time and the runner moves twice as fast as the walker, eventually the runner will lap the walker. If the walker and runner were instead moving along a straight path, the walker would never see the runner again!

Source: [via GIPHY](https://giphy.com/gifs/Boxmedia-aida-milena-marinova-clare-munn-cKKilkePjBAh0tbmBU)

If you think of the slow pointer as the walker and the fast pointer as the runner, we can apply the same logic to say that if the slow pointer and fast pointer have the same value, the fast pointer is "lapping" the slow pointer and there must be a cycle in the list.





Bonus Concepts 💡 Not In-Scope

The following concepts are nice to know and may improve your code readability or help you solve certain problems more easily and efficiently. However, they are not *required* to solve any of the problems in this unit. These concepts are **not in scope for this unit's assessments**, and you do not need to memorize them! Click on each concept to read more about how to use it.

- [**`lst.extend(x)`**](hhttps://www.w3schools.com/python/ref_list_extend.asp) Modifies the given list by appending all elements in iterable `x`.
- [**`lst.reverse()`**](https://www.w3schools.com/python/ref_list_reverse.asp) Reverses the given list.

## Unit 5 Resources

### Session Recordings

Check out our live session recordings:

- [Instructor Led Sessions Playlist](https://vimeo.com/showcase/12241205?fl=so&fe=fs) \| Passcode: **codepath**
- [Study Hall Playlist](https://vimeo.com/showcase/12252539?fl=so&fe=fs) \| Passcode: **codepath**
- [Fix-it Garage Playlist](https://vimeo.com/showcase/12252541?fl=so&fe=fs) \| Passcode: **codepath**

**Note:** It may take up to 24-48 hours after the session has concluded to appear on the playlist.

### Guides & Cheatsheet Links

#### Guides

**Breakout Solutions**

- [Unit 5 Breakout Problem Solutions](https://github.com/codepath/compsci_guides/wiki/TIP103-Unit-5)

#### Cheatsheet

- [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/5#!cheatsheet)

#### Mock Interview Questions

Below is a list of additional interview questions spanning *all units* you can work on for additional practice.

- [Mock Interview Questions](https://courses.codepath.org/snippets/tip103/mock_interview_questions)
