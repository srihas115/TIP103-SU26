# Problem 4: Mewtwo's Genetic Fusion

Professor Oak has tasked you with a challenging experiment: fusing the DNA of two Pokémon, Mew and Ditto, to create a new species! The fusion process is governed by specific rules, where the genetic sequences of Mew (`dna1`) and Ditto (`dna2`) must be interwoven to form a new DNA sequence (`dna3`). Your goal is to determine if `dna3` can be formed by interleaving the sequences of `dna1` and `dna2`.

An interleaving of two genetic sequences `g1` and `g2` is a configuration where the sequences are divided into smaller substrings, and then combined alternately without changing the order of the substrings.

Help Professor Oak figure out if `dna3` can be obtained by interleaving `dna1` and `dna2` by implementing a function `genetic_fusion()` that returns `True` if the fusion is successful and `False` otherwise. 

```python
def genetic_fusion(dna1, dna2, dna3):
    pass
```

Example Usage:

*Example 1:*
![Example 1 showing interleaving of dna1 and dna2](./mewtwos_genetic_fusion.jpg)

```python
print(genetic_fusion("aabcc", "dbbca", "aadbbcbcac"))
print(genetic_fusion("aabcc", "dbbca", "aadbbbaccc"))
print(genetic_fusion("", "", ""))
```

Example Output:

```markdown
True  
Example 1 Explanation:  
One way to obtain `dna3` is:  
Split `dna1` into "aa" + "bc" + "c", and `dna2` into "dbbc" + "a".  
Interleaving the two sequences gives "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".  
Since this forms `dna3`, the result is `True`.

False  
Example 2 Explanation:  
It is impossible to interleave `dna2` with any other string to form `dna3`.

True  
Example 3 Explanation:  
Empty strings can always be interleaved to form an empty string.
```

<details>
  <summary><strong>✨ AI Hint: 2-D Dynamic Programming</strong></summary>

Because the solution to this problem depends on two different variables, we'll need **2-D dynamic programming** to solve this problem.

To learn more about 2-D dynamic programming, try using an AI tool like ChatGPT or GitHub Copilot to explain the topic, both conceptually and with examples in Python. You can also check out the 2-D Dynamic Programming section of the [Unit 12 Cheatsheet](#unit-12-cheatsheet).

Note that 2-D dynamic programming is **only in scope for TIP103 Assessments**. It is just an extra challenge for TIP102 students 😊.

</details>
