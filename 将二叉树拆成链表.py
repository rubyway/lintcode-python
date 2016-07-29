"""


将一棵二叉树按照前序遍历拆解成为一个假链表。所谓的假链表是说，用二叉树的 right 指针，来表示链表中的 next 指针。
注意事项

不要忘记将左儿子标记为 null，否则你可能会得到空间溢出或是时间溢出。
您在真实的面试中是否遇到过这个题？
样例

              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        temp = []
        self.pre_order(root, temp)
        cur = root
        length = len(temp)
        for i in range(1, length):
            tempnode = TreeNode(temp[i])
            cur.left = None
            cur.right = tempnode
            cur = cur.right
        return root


    def pre_order(self, root, temp):
        if root is None:
            return
        temp.append(root.val)
        self.pre_order(root.left, temp)
        self.pre_order(root.right, temp)
"""        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        if root.left is None:
            right = root.right
            self.flatten(right)

        if root.right is None:
            left = root.left
            root.right = left
            self.flatten(left)
            root.left = None
        
        left = root.left
        right = root.right
        root.right = left
        self.flatten(left)
        p = left
        while p.right:
            p = p.right
        p.right = right
        self.flatten(right)
        root.left = None

     #前序遍历：根左右
     #修改根的right指向左部分
     #左部分的right指向右部分"""


