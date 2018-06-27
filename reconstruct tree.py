# reconstruct tree from inorder and postorder traverse
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def reconstructTree(inorder, postorder):

    if not inorder or not postorder or len(inorder) != len(postorder):
        return None
    node = TreeNode(postorder[-1])
    i = inorder.index(postorder[-1])
    node.left = reconstructTree(inorder[:i], postorder[:i])
    node.right = reconstructTree(inorder[i+1:], postorder[i:-1])
    return node
    
def reconstructTreeII(inorder, preorder):

    if not inorder or not preorder or len(inorder) != len(preorder):
        return None
    node = TreeNode(preorder[0])
    i = inorder.index(preorder[0])
    node.left = reconstructTree(inorder[:i], preorder[1:1+i])
    node.right = reconstructTree(inorder[i+1:], preorder[i+1:])
    return node

# always has left subtree
def reconstructTreeIII(postorder, preorder):
    if not postorder or not preorder or len(postorder) != len(preorder):
        return None
    node = TreeNode(preorder[0])
    if len(preorder) > 1:
        left_val = preorder[1]
        index = postorder.index(left_val)
        node.left = reconstructTreeIII(postorder[:index+1], preorder[1:2+index])
        node.right = reconstructTreeIII(postorder[index+1:-1], preorder[2+index:])
    return node
