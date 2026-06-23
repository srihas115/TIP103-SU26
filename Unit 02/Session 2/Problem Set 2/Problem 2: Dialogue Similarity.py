def is_similar(sentence1, sentence2, similar_pairs):
    pass

sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))
