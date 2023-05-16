# Lowest Common Ancestor of a Binary Tree
# 문제에서 Binary 트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다.
# 이 때, 두 노드의 공통 조상 중 가장 낮은 node 즉, the lowest common ancestor (LCA)를 찾아라.

def LCA(root, p, q):
    if root == None:
        return None
    
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right

LCA([3,5,1,6,2,0,8], 6, 4)