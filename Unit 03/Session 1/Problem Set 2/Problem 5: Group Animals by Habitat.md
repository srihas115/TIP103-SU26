# Problem 5: Group Animals by Habitat

You are managing a wildlife sanctuary where animals of the same species need to be grouped together by their habitats. Given a string`habitats`representing the sequence of animals, where each character corresponds to a particular species, you need to partition the string into as many contiguous groups as possible, ensuring that each species appears in at most one group.

The order of species in the resultant sequence must remain the same as in the input string`habitats`.

Return a list of integers representing the size of these habitat groups.

```
def group_animals_by_habitat(habitats):
  pass
```

Example Usage:

```
print(group_animals_by_habitat("ababcbacadefegdehijhklij"))
print(group_animals_by_habitat("eccbbbbdec"))
```

Example Output:

```
[9,7,8]
[10]
```