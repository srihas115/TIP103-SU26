# Problem 4: Casting Call Search

You are a casting agent for a major Hollywood production and the director has a certain celebrity in mind for the lead role. You have an adjacency matrix `celebs` where `celebs[i][j] = 1` means that celebrity `i` has a connection with celebrity `j`, and `celebs[i][j] = 0` means they don't. Connections are directed meaning that `celebs[i][j] = 1` does not automatically mean `celebs[j][i] = 1`. 

Given a celebrity you know `start_celeb` and the celebrity the director wants to hire `target_celeb`, use Breadth First Search to return `True` if you can find a path of connections from `start_celeb` to `target_celeb`. Otherwise, return `False`. 

```python
def have_connection(celebs, start_celeb, target_celeb):
    pass
```

Example Usage:

!['celebs' graph diagram](../../Unit%20Assets/casting_call_search.png)

```python
celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 0
            [1, 0, 1, 0, 0, 0, 0, 0], # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0], # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0], # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]  # Celeb 7
            ]

print(have_connection(celebs, 0, 6))
print(have_connection(celebs, 3, 5))
```

Example Output:

```markdown
True
False
```

<details>
  <summary><strong>✨ AI Hint: Breadth First Search Traversal</strong></summary>

*Key Skill: Use AI to explain code concepts*

To solve this problem, it may be helpful to understand both the **queue** data structure and **breadth first search** algorithm. To learn more about these concepts, visit the Queues and Breadth First Search sections of the Cheatsheet.

If you still have questions, try explaining what you're doing, and ask an AI tool like ChatGPT or GitHub Copilot to help you understand what's confusing you. For example, you might ask:

*"I'm trying to understand how to use a queue to implement breadth first search, but I'm confused about why I wouldn't just use a list. Can you explain the difference?"*

</details>
