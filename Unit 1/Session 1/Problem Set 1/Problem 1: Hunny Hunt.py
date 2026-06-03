# def linear_search(items, target):
# 	for i, item in enumerate(items):
# 		if item == target:
# 			print(i)
# 			return
# 	print(-1)

def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            print(i)
            return
    print(-1)
			

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)