'''
给一个空的BST，只有每个节点的value是空的，其他都正常。同时给一个int数组，是该BST的in order顺序遍历下来的值。要求写个方法填充BST节点value。（没有return value，直接填就可以了）

举例：
    A
   / \. 
  B   C
/ 
D
. from: 
1, 2, 3, 4. 

应该填充成：
    3.
   / \
  2   4
/
1
'''

class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def fillTree(root, nums):
    def pushAll(node):
        while node:
            stack.append(node)
            node = node.left
    stack = []
    index = 0
    pushAll(root)
    while stack:
        node = stack.pop()
        node.val = nums[index]
        index += 1
        if node.right:
            pushAll(node.right)
    return root

def buildTree():
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    return root
    
root = buildTree()
fillTree(root, [1,2,3,4])
print('expect 3, got', root.val)
print('expect 2, got', root.left.val)
print('expect 1, got', root.left.left.val)
print('expect 4, got', root.right.val)
