def max_survival_probability(n, edges, succ_prob, start, end):
    pass

edges_1 = [[0, 1], [1, 2], [0, 2]]
succ_prob_1 = [0.5, 0.5, 0.2]

print(max_survival_probability(3, edges_1, succ_prob_1, 0, 2))

edges_2 = [[0, 1], [1, 2], [0, 2]]
succ_prob_2 = [0.5, 0.5, 0.3]

print(max_survival_probability(3, edges_2, succ_prob_2, 0, 2))

edges_3 = [[0, 1]]
succ_prob_3 = [0.5]

print(max_survival_probability(2, edges_3, succ_prob_3, 0, 1))
