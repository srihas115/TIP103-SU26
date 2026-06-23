class TreeNode():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class TreeNode():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# For testing
def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            if node.next is not None:
                result.append((node.val, node.next.val))
            else:
                result.append((node.val, None))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def connect(root):
    pass

values = [1, 2, 3, 4, 5, 6, 7]

root = build_tree(values)
print_tree(connect(root))
