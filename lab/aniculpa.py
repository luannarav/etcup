class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def find_matching_group(node, target_value):
    current = node
    while current is not None:
        if current.value == target_value:
            return current
        current = current.parent
    return None  # No matching group found

# Example usage:
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)

root.left = child1
root.right = child2
child1.parent = root
child2.parent = root

result = find_matching_group(child1, 1)
if result:
    print("Found matching group:", result.value)
else:
    print("No matching group found")
