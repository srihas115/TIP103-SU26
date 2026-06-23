# Problem 7: Market Token Value

You are a vendor in a mystical market where magical tokens are used for trading. The value of a token is determined by its structure, represented by a string containing pairs of mystical brackets `()`.

The value of a mystical token is calculated based on the following rules:

-   `()` has a value of 1.
-   The value of two adjacent tokens `AB` is the sum of their individual values, where `A` and `B` are valid token structures.
-   The value of a nested token `(A)` is twice the value of the token inside the brackets.

Your task is to calculate the total value of a given mystical token string.

```python
def token_value(token):
  pass
```

Example Usage:

```python
print(token_value("()"))
print(token_value("(())"))
print(token_value("()()"))
```

Example Output:

```
1
2
2
```