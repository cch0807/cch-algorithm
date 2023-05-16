# Traversal (트리 순회)

# Preorder (전위 순회)
def preorder(cur_node):
    if cur_node is None:
        return
    
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

preorder(root)

# Inorder (중위 순회)

def preorder(cur_node):
    if cur_node is None:
        return
    
    preorder(cur_node.left)
    print(cur_node.value)
    preorder(cur_node.right)

preorder(root)

# Postorder (후위 순회)
