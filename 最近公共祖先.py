"""
最近公共祖先

给定一棵二叉树，找到两个节点的最近公共父节点(LCA)。

最近公共祖先是两个节点的公共的祖先节点且具有最大深度。

样例
对于下面这棵二叉树

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7"""
#https://leetcode.com/discuss/45386/4-lines-c-java-python-ruby
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        lista, listb = self.search(root, A), self.search(root, B)
        lentha, lenthb = len(lista), len(listb)
        result, x = None, 0
        while x < min(lentha, lenthb) and lista[x] == listb[x]:
            result, x = lista[x], x + 1
        return result
    def search(self, root, i):#dfs
        templist = []
        visit = None
        while root or templist:
            if root:
                templist.append(root)
                root = root.left
            else:
                top = templist[-1]
                if top.right and visit != top.right:
                    root = top.right
                else:
                    if top == i:
                        return templist
                    visit = templist.pop()
                    root = None
        return templist
        
